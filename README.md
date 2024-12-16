# Motus AI Internship - Completed Tasks

This repository contains the solutions to the three tasks assigned during the Motus AI Internship. The tasks involve pose detection, model optimization for mobile, and real-time human movement tracking.

## Tasks Overview

### 1. Pose Detection Challenge
- **Objective:** Implement a basic pose detection system using a pre-trained model.
- **Details:** The task involved processing a video of a person performing squats and detecting key pose points (e.g., shoulders, hips, knees). We then calculated the knee bend angle in each frame and output the angle sequence.
- **Tools Used:** Mediapipe for pose detection, OpenCV for video processing, Python for scripting.
  
### 2. Mobile Optimization Challenge
- **Objective:** Optimize a given ML model for mobile inference.
- **Details:** The task involved optimizing a pose estimation model (in TensorFlow Lite format) to run efficiently on mobile devices. The model was quantized and inference time was measured and saved.
- **Tools Used:** TensorFlow Lite for model conversion and optimization, OpenCV for video processing, Python for scripting.

### 3. Real-Time Tracking Challenge
- **Objective:** Implement a real-time human movement tracker.
- **Details:** This task involved processing a live webcam feed to detect and track human movement in real-time. A bounding box was drawn around the moving human figure.
- **Tools Used:** Mediapipe for pose detection, OpenCV for webcam feed and visualization, Python for scripting.

## Requirements

- Python 3.x
- TensorFlow
- Mediapipe
- OpenCV
- NumPy

You can install the required dependencies using `pip`:

```bash
pip install tensorflow mediapipe opencv-python numpy
```

# Setup and Execution
## Task 1: Pose Detection Challenge

1. Clone the repository.
2. Place the input video file (squat.mp4) in the same directory as the script.
3. Run the script to detect pose landmarks and calculate the knee bend angle:
```bash
 python pose_detection.py
```
This will output the angles for each frame in angles.txt.

## Task 2: Mobile Optimization Challenge
1. Clone the repository.
2. Quantize the TensorFlow Lite model for mobile devices using the provided script.
3. Run the script to load the quantized model and process a video:
```bash
python mobile_optimization.py
```
This will display inference times for each frame and print them to the console.

## Task 3: Real-Time Tracking Challenge
1. Clone the repository.
2. Connect a webcam or use a virtual webcam.
3. Run the script to track human movement in real-time and draw a bounding box around the detected human:
```bash
python real_time_tracking.py
```
Press 'q' to exit the webcam feed.

# File Structure
```graphql
Motus-AI-Task/
│
├── pose_detection.py          # Script for Pose Detection Challenge
├── mobile_optimization.py     # Script for Mobile Optimization Challenge
├── real_time_tracking.py      # Script for Real-Time Tracking Challenge
├── squat.mp4                  # Example input video for pose detection (Optional)
├── angles.txt                 # Output file with calculated knee angles
├── model.tflite               # Quantized TensorFlow Lite model (Optional)
└── README.md                  # This README file
```