import boto3
import pandas as pd

# Specify your AWS credentials
access_key = ''#your AWS access key
secret_key = ''#your AWS secret key
region_name = ''#your AWS region name

# Initialize the session and client
session = boto3.Session(aws_access_key_id=access_key, aws_secret_access_key=secret_key, region_name=region_name)
s3_client = session.client('s3')

# Specify the S3 bucket and video file name
bucket_name = 'vanilla3230'
video_file = 'Video.mp4'

# Initialize the Rekognition client
rekognition_client = session.client('rekognition')

# Specify the S3 bucket and video file
video = {'S3Object': {'Bucket': bucket_name, 'Name': video_file}}

# Specify the parameters for the face detection operation
response = rekognition_client.start_face_detection(Video=video, FaceAttributes='ALL')

# Retrieve the job ID for the face detection operation
job_id = response['JobId']

# Wait for the operation to complete
while True:
    response = rekognition_client.get_face_detection(JobId=job_id, MaxResults=1000)
    status = response['JobStatus']
    if status == 'SUCCEEDED':
        break
    elif status == 'FAILED':
        raise Exception('Face detection failed')

# Create a DataFrame object to store the detected faces
data = [
    [
        face_detection['Timestamp'],
        face_detection['Face']['BoundingBox']['Left'],
        face_detection['Face']['BoundingBox']['Top'],
        face_detection['Face']['BoundingBox']['Width'],
        face_detection['Face']['BoundingBox']['Height'],
        (face_detection['Face']['AgeRange']['Low'] + face_detection['Face']['AgeRange']['High']) / 2,
        face_detection['Face']['Gender']['Value'],
        face_detection['Face']['Emotions'][0]['Type'],
        face_detection['Face']['Emotions'][0]['Confidence']
    ]
    for face_detection in response['Faces']
]

columns = [
    'Timestamp', 'Left', 'Top', 'Width', 'Height', 'Age', 'Gender', 'Emotion', 'Confidence'
]

df = pd.DataFrame(data, columns=columns)

# Print the DataFrame object
print(df.head(1))