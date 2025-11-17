import requests
import json

# 🧠 Replace this with your Gemini API Key
API_KEY = "AIzaSyD1aYkhDPutwphtLJrPu1PaQ0zSceYRCo8"

# 📡 Google Gemini endpoint to list all models
url = f"https://generativelanguage.googleapis.com/v1beta/models?key={API_KEY}"

print("🔍 Checking available Gemini models...\n")

try:
    response = requests.get(url)

    if response.status_code == 200:
        models_data = response.json()

        print("✅ Available Gemini Models:\n")
        for model in models_data.get("models", []):
            print(f"🧩 Model Name: {model['name']}")
            print(f"📘 Display Name: {model.get('displayName', 'N/A')}")
            print(f"📝 Description: {model.get('description', 'No description provided')}\n")

        # Save result to a file for reference
        with open("available_gemini_models.json", "w", encoding="utf-8") as f:
            json.dump(models_data, f, indent=4)
            print("💾 Saved model list to available_gemini_models.json")

    else:
        print(f"❌ Error {response.status_code}: {response.text}")

except requests.exceptions.RequestException as e:
    print(f"🚫 Connection Error: {e}")
