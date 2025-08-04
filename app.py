# app.py
# UtsavaMitra - Indian Festivals Chatbot (Replies in Telugu text)
# Built with Gradio + OpenAI - No audio
from dotenv import load_dotenv
import json
import os
import openai
import gradio as gr


load_dotenv()
# ========================
# 1. Load OpenAI API Key
# ========================
openai.api_key = os.getenv("OPENAI_API_KEY")
if not openai.api_key:
    raise ValueError("OPENAI_API_KEY is missing. Set it in Hugging Face Secrets.")

# ========================
# 2. Load Festival Data
# ========================
try:
    with open('festivals.json', 'r', encoding='utf-8') as f:
        festivals_data = json.load(f)
except FileNotFoundError:
    festivals_data = []
    print("Warning: festivals.json not found. Using empty list.")
except json.JSONDecodeError:
    festivals_data = []
    print("Error: festivals.json is not valid JSON.")

# ========================
# 3. Search Festival Info
# ========================
def get_festival_info(query):
    query = query.lower().strip()
    for festival in festivals:
        if query in festival['name'].lower() or query in festival['english_name'].lower():
            return festival['description']
    return None

# ========================
# 4. Generate Telugu Response
# ========================
def generate_telugu_response(user_query):
    description = get_festival_info(user_query)
    
    if description:
        prompt = f"Explain this festival: {description}. Respond in simple Telugu."
    else:
        prompt = (
            f"Explain an Indian festival based on: '{user_query}'. "
            "Respond in friendly, simple Telugu. Include when, where, and how it's celebrated."
        )

    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are UtsavaMitra, a helpful AI that answers questions about Indian festivals in Telugu. Always reply in Telugu."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            max_tokens=200,
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except openai.AuthenticationError:
        return "❌ Invalid or missing OpenAI API key. Please check your settings."
    except openai.APIError as e:
        return f"❌ OpenAI server error: {str(e)}"
    except Exception as e:
        return f"❌ Failed to generate response: {str(e)}"

# ========================
# 5. Main Chat Function
# ========================
def utsavamitra_chat(query):
    if not query or not query.strip():
        return "Please enter a valid question."
    return generate_telugu_response(query.strip())

# ========================
# 6. Gradio Interface
# ========================
demo = gr.Interface(
    fn=utsavamitra_chat,
    inputs=gr.Textbox(
        placeholder="Example: Tell me about Diwali",
        label="Your Question",
        lines=2
    ),
    outputs=gr.Textbox(
        label="UtsavaMitra Response",
        lines=6,
        placeholder="Response will appear here..."
    ),
    title="🎉 UtsavaMitra - Festival Friend",
    description="Ask about Indian festivals and get answers in Telugu!",
    theme="huggingface",
    allow_flagging="never",
    examples=[
        ["Tell me about Diwali"],
        ["When is Ugadi?"],
        ["What is Pongal?"]
    ]
)

# ========================
# 7. Launch App
# ========================
if __name__ == "__main__":
    demo.launch()
