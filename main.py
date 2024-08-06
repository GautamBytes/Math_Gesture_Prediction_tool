import cvzone
import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import google.generativeai as genai
from PIL import Image
import streamlit as st

# Streamlit setup
st.set_page_config(layout="wide")
st.image('MathGestures.png')

col1, col2 = st.columns([3, 2])
with col1:
    run = st.checkbox('Run', value=True)
    FRAME_WINDOW = st.image([])

with col2:
    st.title("Answer")
    output_text_area = st.subheader("")

# Configure AI model
genai.configure(api_key="AIzaSyBGLCoU9-k5sA9e1Y3N96JcoNa0jymbJSQ")
model = genai.GenerativeModel('gemini-1.5-flash')

# Initialize webcam with the correct index
camera_index = 0 # Replace with the correct index found using the list_cameras script
cap = cv2.VideoCapture(camera_index)
cap.set(3, 1280)
cap.set(4, 720)

# Hand detector setup
detector = HandDetector(staticMode=False, maxHands=1, modelComplexity=1, detectionCon=0.8, minTrackCon=0.7)

def getHandInfo(img):
    hands, img = detector.findHands(img, draw=False, flipType=True)
    if hands:
        hand = hands[0]
        lmList = hand["lmList"]
        fingers = detector.fingersUp(hand)
        return fingers, lmList
    else:
        return None

def draw(info, prev_pos, canvas):
    fingers, lmList = info
    current_pos = None
    if fingers == [0, 1, 0, 0, 0]:  # Index finger up
        current_pos = lmList[8][0:2]
        if prev_pos is not None:
            cv2.line(canvas, prev_pos, current_pos, (0, 255, 0), 10)  # Use dark green color
        prev_pos = current_pos
    else:
        prev_pos = None  # Reset previous position if the index finger is not up
    if fingers == [1, 0, 0, 0, 0]:  # Thumb up
        canvas = np.zeros_like(canvas)
        prev_pos = None  # Reset previous position when clearing the canvas
    return prev_pos, canvas

def sendToAI(model, canvas, fingers):
    if fingers == [1, 1, 1, 1, 0]:  # Four fingers up (excluding pinky)
        pil_image = Image.fromarray(canvas)
        # Convert the image to black and white to improve recognition
        pil_image = pil_image.convert('L')
        response = model.generate_content(["Solve this math problem", pil_image])
        return response.text
    return ""

prev_pos = None
canvas = None
image_combined = None
output_text = ""

while run:
    success, img = cap.read()
    if not success:
        st.error("Failed to read from webcam. Please check the camera index and connection.")
        break
    
    img = cv2.flip(img, 1)

    if canvas is None:
        canvas = np.zeros_like(img)

    info = getHandInfo(img)
    if info:
        fingers, lmList = info
        prev_pos, canvas = draw(info, prev_pos, canvas)
        output_text = sendToAI(model, canvas, fingers)

    image_combined = cv2.addWeighted(img, 0.7, canvas, 0.3, 0)
    FRAME_WINDOW.image(image_combined, channels="BGR")

    if output_text:
        output_text_area.text(output_text)

    cv2.waitKey(1)



