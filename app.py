# app.py
import os
import json
import google.generativeai as genai
from langdetect import detect
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-pro")

# Load festival data
with open("festivals.json", "r", encoding="utf-8") as f:
    festivals = json.load(f)

def detect_language(text):
    """Detect if input is Telugu or English"""
    try:
        lang = detect(text)
        return "te" if lang == "te" else "en"
    except:
        return "en"  # fallback to English

def get_festival_info(query):
    """Search festival by name in Telugu or English"""
    query_lower = query.lower()
    for fest in festivals:
        if (query_lower in fest["name"].lower() or 
            query_lower in fest["english_name"].lower()):
            return fest
    return None

def generate_response(user_input):
    """Generate response using database + AI"""
    lang = detect_language(user_input)
    
    # First, check if it's a direct festival query
    festival = get_festival_info(user_input)
    
    if festival:
        if lang == "te":
            return f"**{festival['name']}**: {festival['description_te']}"
        else:
            return f"**{festival['english_name']}**: {festival['description_en']}"
    
    # If not found, use AI to answer
    prompt = f"""
    You are 'ఉత్సవ మిత్ర', a friendly AI chatbot that helps users learn about Indian festivals, especially those in Telangana.
    Respond in {'Telugu' if lang == 'te' else 'English'}.
    Be informative and warm.
    
    User asked: {user_input}
    
    Answer:
    """
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return "Sorry, I couldn't process your request. Please try again."

# Test in terminal
if __name__ == "__main__":
    print("🎉 ఉత్సవ మిత్ర ప్రారంభమైంది! (Utsava Mitra started!)\n")
    print("Type 'exit' to quit.\n")
    
    while True:
        user = input("You: ")
        if user.lower() in ["exit", "quit", "బయలుదేరు"]:
            print("ఉత్సవ మిత్ర: సురక్షిత ప్రయాణం! 🙏")
            break
        reply = generate_response(user)
        print(f"ఉత్సవ మిత్ర: {reply}\n")