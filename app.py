import streamlit as st
import requests

st.set_page_config(page_title="StudyAid - AI Video Generator", page_icon="🎥", layout="centered")

BACKEND_URL = "http://127.0.0.1:8000/upload/"

st.title("🎓 StudyAid: AI-Powered Educational Video Creator")
st.write("Upload an image, PDF, or enter text to generate an animated educational video using AI!")

uploaded_file = st.file_uploader("Upload your file (Image/PDF)", type=["png", "jpg", "jpeg", "pdf"])

if st.button("Generate Educational Video"):
    if uploaded_file is not None:
        with st.spinner("Processing your file... ⏳"):
            files = {"file": uploaded_file.getvalue()}
            res = requests.post(BACKEND_URL, files=files)
            
            if res.status_code == 200:
                data = res.json()
                st.success("✅ Video Generated Successfully!")
                st.subheader("Extracted Text:")
                st.write(data.get("extracted_text", ""))
                st.subheader("AI Narration:")
                st.write(data.get("ai_prompt", ""))
                st.video(data.get("video_path", "generated_video.mp4"))
            else:
                st.error(f"Error: {res.text}")
    else:
        st.warning("Please upload a file first!")