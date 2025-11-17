import os
import requests
import streamlit as st

# ✅ Gemini API details
GEMINI_API_KEY = "AIzaSyD1aYkhDPutwphtLJrPu1PaQ0zSceYRCo8"
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"

def generate_video_prompt(text: str) -> str:
    """Call Gemini API safely to generate an educational script"""
    headers = {"Content-Type": "application/json"}
    payload = {
        "contents": [{
            "parts": [{"text": f"Create an engaging educational video narration script for:\n\n{text}"}]
        }]
    }

    try:
        res = requests.post(f"{GEMINI_API_URL}?key={GEMINI_API_KEY}", headers=headers, json=payload)
        
        # 🛑 If not OK, display readable error
        if res.status_code != 200:
            st.error(f"❌ Gemini API Error ({res.status_code}): {res.text}")
            return ""
        
        # ✅ Handle JSON safely
        try:
            data = res.json()
            return data["candidates"][0]["content"]["parts"][0]["text"]
        except Exception:
            st.error("⚠️ Gemini returned an unexpected response. Try again later.")
            return ""
            
    except requests.exceptions.RequestException as e:
        st.error(f"🚫 Network Error: {e}")
        return ""

# 🧠 Streamlit App
st.set_page_config(page_title="AI Study Aid - Script Generator", page_icon="🎓", layout="centered")
st.title("🎥 AI Study Aid - Educational Video Script Generator")
st.write("Paste your topic or content and get a natural educational narration script.")

text_input = st.text_area("Enter your topic or paste text content:", height=200)

if st.button("Generate Script"):
    if text_input.strip():
        with st.spinner("⏳ Generating your educational script..."):
            script = generate_video_prompt(text_input)
        if script:
            st.subheader("📜 Generated Script:")
            st.success(script)
    else:
        st.warning("Please enter some text first!")

st.caption("🚀 Built with ❤️ using Gemini API and Streamlit.")
