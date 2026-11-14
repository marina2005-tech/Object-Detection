# Object Detection Project

##  Overview
This project is a real-time-style object detection and tracking application built using **Python, OpenCV, and Streamlit**.

It uses background subtraction to detect moving objects in uploaded videos and highlights detected objects using green bounding boxes.

## 🚀 Features
- Upload videos in MP4, AVI, and MOV formats.
- Apply background subtraction using OpenCV's MOG2 algorithm.
- Extract foreground objects from video frames.
- Detect objects using contour detection.
- Filter small objects based on contour area.
- Draw green bounding boxes around detected objects.
- Display the foreground image and tracked objects side by side.

##  Technologies Used
- **Python** – Main programming language.
- **OpenCV (cv2)** – Video processing, background subtraction, and object detection.
- **NumPy** – Numerical operations.
- **Matplotlib** – Plotting library.
- **Streamlit** – Web application interface.
- **Tempfile** – Temporarily stores uploaded video files.

##  Project Structure

```text
Object Detection/
│
├── app.py
├── requirements.txt
├── README.md
└── .venv/
```

##  Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/marina2005-tech/Object-Detection.git
```

### 2. Navigate to the project directory

```bash
cd Object-Detection
```

### 3. Create a virtual environment (optional)

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

**Windows:**

```bash
.venv\Scripts\activate
```

### 5. Install the required libraries

```bash
pip install -r requirements.txt
```

If you don't have a requirements file, install the libraries using:

```bash
pip install opencv-python numpy matplotlib streamlit
```

### 6. Run the application

```bash
streamlit run app.py
```

The application will open in your default web browser.

## 🔍 How It Works

1. **Video Upload:** The user uploads a video through the Streamlit interface.
2. **Video Processing:** OpenCV reads the uploaded video frame by frame.
3. **Background Subtraction:** The MOG2 background subtractor separates moving foreground objects from the background.
4. **Contour Detection:** Contours are extracted from the foreground image.
5. **Object Filtering:** Only contours with an area greater than 500 pixels are considered.
6. **Object Tracking Visualization:** Green bounding boxes are drawn around the detected objects.
7. **Display Results:** The application displays the foreground image and the video frame containing detected objects side by side.

##  Algorithm Used

**Background Subtraction – MOG2**

The project uses OpenCV's `createBackgroundSubtractorMOG2()` method to identify moving objects by separating the foreground from the background.

**Contour Detection**

The `findContours()` function detects the boundaries of foreground objects.

**Bounding Boxes**

The `boundingRect()` function calculates rectangular boundaries around detected objects, and `rectangle()` draws green boxes around them.

## Author

**Marina Youssef**

Object Detection Project – Python and Computer Vision.
