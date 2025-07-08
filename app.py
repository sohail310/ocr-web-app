import streamlit as st
import cv2
import pytesseract
from PIL import Image
import numpy as np

# DO NOT set tesseract_cmd on Streamlit Cloud — it uses default Linux path

st.title("🧠 OCR Web App - Text Extraction from Image")
st.markdown("Upload an image and extract printed text using Tesseract OCR engine.")

uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    img_cv = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    text = pytesseract.image_to_string(thresh)
    st.subheader("📝 Extracted Text:")
    st.text_area("Output", text, height=250)
    st.download_button("📥 Download as .txt", data=text, file_name="extracted_text.txt")

st.markdown("---")
st.markdown("👨‍💻 Developed by **Suhail Syed**")
