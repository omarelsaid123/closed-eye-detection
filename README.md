💤 Real-Time Eye Status Detection using MediaPipe and OpenCV
This project uses MediaPipe's Face Mesh and OpenCV to detect whether a user's eyes are open or closed in real time using a webcam. It draws facial landmarks on the eyes and logs the status ("Eyes OPEN" or "Eyes CLOSED") to a text file whenever a change in state is detected.

📸 How It Works
Uses MediaPipe Face Mesh to get precise facial landmarks.

Monitors vertical distances between key points around each eye.

Compares distances against a threshold to determine if the eyes are closed.

Logs the change in eye state to eye_log.txt.

Displays the live camera feed with eye landmarks.

📁 Files
Closed-eye-detector.py – Main Python script that runs the detection.

eye_log.txt – Auto-generated file logging eye state changes.

🔧 Requirements
Python 3.7+

OpenCV

MediaPipe

Install dependencies:
pip install opencv-python mediapipe

▶️ Run the Program
Press q to quit the program.

💡 Use Cases
Drowsiness detection

Focus/attention tracking

Human-computer interaction projects

📌 Features
Real-time detection

Uses MediaPipe's accurate facial landmarks

Fully resizable OpenCV window

Simple threshold-based logic (easy to fine-tune)


