import streamlit as st
import cv2
import numpy as np
import imutils
import easyocr
from PIL import Image 
import os
os.environ['TORCH_BACKEND'] = "cpu"

def extract_license_plate(img_path):
    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    filter = cv2.bilateralFilter(gray, 11, 17, 17)
    edge = cv2.Canny(filter, 30, 200)
    ext_count = cv2.findContours(edge.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    contours = imutils.grab_contours(ext_count)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]
    location = None

    for contour in contours:
        apprx = cv2.approxPolyDP(contour, 10, True)
        if len(apprx) == 4:
            location = apprx
            break

    msk = np.zeros(gray.shape, np.uint8)
    extracted_plate = cv2.drawContours(msk, [location], 0, 255, -1)
    extracted_plate = cv2.bitwise_and(img, img, mask=msk)

    (x, y) = np.where(msk == 255)
    (x1, y1) = (np.min(x), np.min(y))
    (x2, y2) = (np.max(x), np.max(y))
    final_plate = gray[x1:x2 + 1, y1:y2 + 1]
    
    reader = easyocr.Reader(['bn'])  # Here, you might want to use 'en' if the license plates are in English
    detected = reader.readtext(final_plate)
    return detected

st.title("Bengali License Plate Recognition")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])
if uploaded_file is not None:
    image = Image.open(uploaded_file).convert('RGB')
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.image(image, caption='Uploaded Image.', use_column_width=True)

    with col2:
        st.write("")
        st.write("Detecting...")
        with st.spinner('Extracting License Plate...'):
            img_path = "temp_img.jpg"
            image.save(img_path)
            detected_plate = extract_license_plate(img_path)

        if detected_plate:
            st.write(f"License Number: {detected_plate[0][-2]} {detected_plate[1][-2]}")
        else:
            st.write("License Plate Not Detected!")