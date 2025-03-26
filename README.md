# 🎯 AWS Rekognition - Object and Face Detection

This repository contains Python scripts to use **AWS Rekognition** for detecting objects in images 🖼️ and faces in videos 🎥, displaying results with bounding boxes 🟦, and storing face detection results in a **pandas** DataFrame 📊.

---

## 📌 Table of Contents

- [📜 Introduction](#-introduction)
- [⚙️ Prerequisites](#%EF%B8%8F-prerequisites)
- [📥 Installation](#-installation)
- [🚀 Usage](#-usage)
    - [📸 Object Detection in Images](#-object-detection-in-images)
    - [🎭 Face Detection in Videos](#-face-detection-in-videos)
- [📜 License](#-license)

---

## 📜 Introduction

This repository provides **two** main functionalities using AWS Rekognition:

1. **🖼️ Object Detection in Images**: Detects objects in an image and visualizes them with bounding boxes.
2. **🎭 Face Detection in Videos**: Detects faces in a video stored in an **S3 bucket**, retrieves detailed information about the faces, and stores the results in a **pandas DataFrame**.

---

## ⚙️ Prerequisites

✅ AWS account with **Rekognition** and **S3 services** enabled.  
✅ AWS credentials 🔑  
✅ Python **3.x** installed 🐍  
✅ Required Python packages 📦:
   - `boto3` 🤖
   - `pandas` 📊
   - `matplotlib` 📈
   - `Pillow` 🖼️

---

## 📥 Installation

1️⃣ **Clone** the repository:
```bash
git clone https://github.com/yourusername/aws-rekognition-detection.git
cd aws-rekognition-detection
```

2️⃣ **Install** the required packages:
```bash
pip install boto3 pandas matplotlib Pillow
```

---

## 🚀 Usage

### 📸 Object Detection in Images

1️⃣ **Update** the script `detect_objects.py` with the **absolute paths** of your AWS credentials CSV file and the image file:
```python
credentials_path = r'path/to/your/credentials.csv'
photo_path = r'path/to/your/photo.jpg'
```

2️⃣ **Run** the script:
```bash
python detect_objects.py
```

3️⃣ The script will **display the image** with bounding boxes around the detected objects 🟦.

---

### 🎭 Face Detection in Videos

1️⃣ **Update** the script `detect_faces.py` with your **AWS credentials**, **region name**, **S3 bucket name**, and **video file name**:
```python
access_key = 'your-aws-access-key'
secret_key = 'your-aws-secret-key'
region_name = 'your-aws-region-name'
bucket_name = 'your-s3-bucket-name'
video_file = 'your-video-file.mp4'
```

2️⃣ **Run** the script:
```bash
python detect_faces.py
```

3️⃣ The script will **print the first row** of the DataFrame containing the detected faces' information 📊.

---

## 📜 License

📄 This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details. 🔖

---

## 👥 Authors

### Vishvam Joshi  
[![GitHub](https://img.shields.io/badge/GitHub-000?logo=github&logoColor=white)](https://github.com/vishvam12a)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?logo=linkedin&logoColor=white)](https://linkedin.com/in/vishvam-j-joshi) 
[![Instagram](https://img.shields.io/badge/Instagram-E4405F?logo=instagram&logoColor=white)](https://instagram.com/vishvam.joshi.71)

### Pragnesh Singh  
[![GitHub](https://img.shields.io/badge/GitHub-000?logo=github&logoColor=white)](https://github.com/pragnesh-singh-rajput)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?logo=linkedin&logoColor=white)](https://linkedin.com/in/pragnesh-singh-rajput) 
[![Instagram](https://img.shields.io/badge/Instagram-E4405F?logo=instagram&logoColor=white)](https://instagram.com/pragnesh_singh_rajput)

### Hardik Singh  
[![GitHub](https://img.shields.io/badge/GitHub-000?logo=github&logoColor=white)](https://github.com/singhhardik531)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?logo=linkedin&logoColor=white)](https://linkedin.com/in/hardik--singh) 
[![Instagram](https://img.shields.io/badge/Instagram-E4405F?logo=instagram&logoColor=white)](https://instagram.com/imhardiksinghh)
