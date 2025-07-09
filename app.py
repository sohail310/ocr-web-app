import streamlit as st
import cv2
import pytesseract
from PIL import Image
import numpy as np

st.title("🌐 Multilingual OCR - Camera & Upload")
st.markdown("Upload an image or take a photo to extract text using Tesseract OCR in your selected language.")

# Select OCR language
languages = {
    "English": "eng",
    "Hindi (हिंदी)": "hin",
    "Telugu (తెలుగు)": "tel",
    "Urdu (اردو)": "urd",
    "Tamil (தமிழ்)": "tam",
    "Kannada (ಕನ್ನಡ)": "kan",
    "Malayalam (മലയാളം)": "mal"
}
selected_lang = st.selectbox("Choose OCR Language", list(languages.keys()))
ocr_lang_code = languages[selected_lang]

# Select image source
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
    text = pytesseract.image_to_string(thresh, lang=ocr_lang_code)
    st.subheader("📝 Extracted Text:")
    st.text_area("Output", text, height=250)
    st.download_button("📥 Download as .txt", data=text, file_name="extracted_text.txt")

st.markdown("---")
st.markdown("👨‍💻 Developed by **Sohail**")
