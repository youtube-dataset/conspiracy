import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

def llm_response():
    print("Sending request to Gemini API...")
    stream = client.interactions.create(
        model="gemini-3.8-flash",
        input="Introduce yourself in a few words",
    )

    print("Stream connected, awaiting chunks...")
    for event in stream:
        # Print raw event or delta text
        if hasattr(event, "delta") and event.delta:
            print(event.delta, end="", flush=True)
        else:
            print(event)

if __name__ == "__main__":
    llm_response()