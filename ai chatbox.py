import os
import requests
from dotenv import load_dotenv


load_dotenv()
HF_API_TOKEN = os.getenv("HF_API_TOKEN")


API_URL = "https://api-inference.huggingface.com/models/tiiuae/falcon-7b-instruct"


headers = {
    "Authorization": f"Bearer {HF_API_TOKEN}",
    "Content-Type": "application/json"
}


def query(prompt):
    payload = {
        "inputs": prompt,
        "parameters": {"max_new_tokens": 100}
    }
    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        output = response.json()
        return output[0]["generated_text"]
    except Exception as e:
        print("Error:", e)
        print("Raw response:", response.text)
        return "[No valid response]"


print("🤖 Chatbot is ready. Type 'exit' to quit.\n")
chat_history = ""

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Chatbot: Goodbye!")
        break

    prompt = f"{chat_history}\nUser: {user_input}\nAssistant:"
    answer = query(prompt)
    print("Chatbot:", answer)
    chat_history += f"\nUser: {user_input}\nAssistant: {answer}"