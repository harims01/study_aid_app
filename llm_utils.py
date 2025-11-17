import google.generativeai as genai

# Configure your Google Gemini API key
genai.configure(api_key="AIzaSyD1aYkhDPutwphtLJrPu1PaQ0zSceYRCo8")

# Load the Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

def generate_video_prompt(text):
    """
    Generate a simple educational video explanation
    from textbook content using Gemini API.
    """
    prompt = f"Explain the following content clearly and simply for a student-friendly animated video:\n\n{text}"
    response = model.generate_content(prompt)
    return response.text
