import boto3
import csv
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import io

# Specify the absolute paths
credentials_path = r'' #path of .csv file in inverted commas
photo_path = r'' #path of image file in inverted commas

# Read AWS credentials from the CSV file
with open(credentials_path, 'r') as file:
    next(file)
    reader = csv.reader(file)

    for line in reader:
        access_key_id = line[2]
        secret_access_key = line[3]

        # Assuming there's only one line in the CSV file, break out of the loop
        break

# Create a Boto3 client for Amazon Rekognition
client = boto3.client('rekognition', region_name='us-east-1', aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key)

# Read the image file
with open(photo_path, 'rb') as image_file:
    source_bytes = image_file.read()


# Detect labels in the image using Amazon Rekognition
detect_objects = client.detect_labels(Image={'Bytes': source_bytes})

# Open image using PIL
image = Image.open(io.BytesIO(source_bytes))

# Increase figure size for better visibility
plt.figure(figsize=(10, 8))

# Create subplot
ax = plt.subplot(111)

# Display the image
ax.imshow(image)

# Extract label data from the response and draw bounding boxes
for label in detect_objects['Labels']:
    # Check if instances exist for the label
    if 'Instances' in label and label['Instances']:
        # Keep track of vertical position for labels
        vertical_offset = 0

        for instance in label['Instances']:
            # Get bounding box information
            box = instance['BoundingBox']
            width, height = image.size

            # Convert bounding box coordinates to pixel values
            left = width * box['Left']
            top = height * box['Top']
            box_width = width * box['Width']
            box_height = height * box['Height']

            # Create a rectangle patch with transparency
            rect = patches.Rectangle((left, top), box_width, box_height, linewidth=1, edgecolor='r', facecolor='none', alpha=0.5)

            # Add the rectangle to the subplot
            ax.add_patch(rect)

            # Adjust label position to prevent overlap
            label_text = label['Name']
            bbox_props = dict(boxstyle="round,pad=0.3", fc="white", ec="black", lw=0.5, alpha=0.8)
            ax.text(left, top + vertical_offset, label_text, fontsize=8, color='r', verticalalignment='top', bbox=bbox_props)

            # Increment the vertical offset
            vertical_offset += 15  # You can adjust this value to increase or decrease the spacing between labels

    else:
        print(f"No instances detected for label: {label['Name']}")

# Add title to the plot
plt.title('Object Detection with Amazon Rekognition')

# Remove the axis to have a clean output
ax.axis('off')

# Show the plot
plt.show()
