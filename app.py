import streamlit as st
import cv2
import pytesseract
from PIL import Image
import numpy as np

# Set Tesseract path (update if installed elsewhere)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# App title
st.title("🧠 OCR Web App - Text Extraction from Image By Sohail.")
st.markdown("Upload an image and extract printed text using Tesseract OCR engine.")

# File uploader
uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Open image with PIL
    image = Image.open(uploaded_file)
    
    # Convert to OpenCV format
    img_cv = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # OCR
    text = pytesseract.image_to_string(thresh)

    # Show result
    st.subheader("📝 Extracted Text:")
    st.text_area("Output", text, height=250)

    # Download button
    st.download_button("📥 Download as .txt", data=text, file_name="extracted_text.txt")

# Footer
# st.markdown("---")
# st.markdown("👨‍💻 Developed by **Sohail**")
