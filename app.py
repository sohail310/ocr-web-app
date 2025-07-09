import streamlit as st
import cv2
import pytesseract
from PIL import Image
import numpy as np

st.title("📸 OCR Web App - Extract Text from Camera or Uploaded Image By Sohail")
st.markdown("Use your **camera** or upload an image to extract printed text using Tesseract OCR.")

# Enable camera input or file upload
image_source = st.radio("Select Image Source", ["📁 Upload Image", "📷 Use Camera"])

image = None

if image_source == "📁 Upload Image":
    uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
elif image_source == "📷 Use Camera":
    captured_image = st.camera_input("Take a photo")
    if captured_image is not None:
        image = Image.open(captured_image)

if image is not None:
    img_cv = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    text = pytesseract.image_to_string(thresh)
    st.subheader("📝 Extracted Text:")
    st.text_area("Output", text, height=250)
    st.download_button("📥 Download as .txt", data=text, file_name="extracted_text.txt")

# st.markdown("---")
# st.markdown("👨‍💻 Developed by **Suhail Syed**")
