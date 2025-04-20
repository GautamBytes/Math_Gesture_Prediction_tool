# Math Gesture Prediction Tool

A real‑time math problem drawing and solving tool using hand gestures and Google’s Gemini AI.\
Draw math expressions in front of your webcam using your index finger, clear the canvas with your thumb, and show four fingers to send the drawing to the AI for solving.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Local Setup](#local-setup)
  - [1. Clone the Repository](#1-clone-the-repository)
  - [2. Create & Activate Virtual Environment](#2-create--activate-virtual-environment)
  - [3. Install Dependencies](#3-install-dependencies)
  - [4. Configure Environment Variables](#4-configure-environment-variables)
  - [5. Detect Your Camera Index](#5-detect-your-camera-index)
  - [6. Update ](#6-update-mainpy-optional)[`main.py`](#6-update-mainpy-optional)[ (Optional)](#6-update-mainpy-optional)
- [Running the App](#running-the-app)
- [How to Use](#how-to-use)
- [Troubleshooting](#troubleshooting)
---

## Features

- **Hand Tracking & Drawing**\
  Utilizes `cvzone` + MediaPipe to detect your hand, track finger position, and draw on a transparent canvas.
- **AI‑Powered Math Solver**\
  Sends your hand‑drawn math problem to Google Gemini (via `google-generativeai`) for instant solutions.
- **Interactive Web UI**\
  Built with Streamlit for a seamless webcam feed + drawing overlay and solution display.

## Prerequisites

- Python 3.8+
- A webcam supported by `imageio` / OpenCV
- A Google Gemini API key (called `GEMINI_API_KEY`)

## Local Setup

### 1. Clone the Repository

```bash
git clone https://github.com/GautamBytes/Math_Gesture_Prediction_tool.git
cd Math_Gesture_Prediction_tool
```

### 2. Create & Activate Virtual Environment

#### Windows (Command Prompt)

```bat
python -m venv .venv
.\.venv\Scripts\activate
```

#### Windows (PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

#### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Configure Environment Variables

To generate a Gemini API key, visit:

```text
https://aistudio.google.com/app/apikey
```

Then create a file named `.env` in the project root with the following content:

```dotenv
GEMINI_API_KEY=your_google_gemini_api_key_here
```

> **Note:** Do **not** commit your `.env` file to version control.

### 5. Detect Your Camera Index

Run the provided camera‑listing script to find your webcam’s index:

```bash
python list_cameras_imageio.py
```

You’ll see output like:

```
Index 0: Camera found
Index 1: Camera not found, error: ...
```

> Remember the index where “Camera found” appears (commonly `0` or `1`).

### 6. Update `main.py` (Optional)

If your camera index is not `0`, open `main.py` and update:

```python
camera_index = 0  # ← change to the index found above
```

---

## Running the App

```bash
streamlit run main.py
```

- The browser will open at `http://localhost:8501` by default.
- To specify a different port, add `--server.port <PORT>` to the command.

## How to Use

1. **Draw**
   - Raise **index finger** to draw lines on the canvas.
2. **Clear**
   - Show **thumb up** gesture to reset/clear the canvas.
3. **Solve**
   - Show **four fingers** (all but pinky) to send the current drawing to Google Gemini for solving.
   - The AI’s solution appears in the right‑hand pane.

> Expand the “How to use” panel in the app for these same instructions.

## Troubleshooting

- **No camera detected**
  - Double‑check the camera index via `list_cameras_imageio.py`.
  - Ensure no other app is blocking the webcam.
- **`GEMINI_API_KEY`**\*\* not found\*\*
  - Confirm your `.env` file is in the project root.
  - Restart the Streamlit server after updating `.env`.
- **Slow or inconsistent detection**
  - Improve lighting & background contrast.
  - Reduce `modelComplexity` or lower detection thresholds in `HandDetector`.
