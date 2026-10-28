from google import genai

client = genai.Client()

stream = client.interactions.create(
    model= "gemini-3.8-flash",
    input= "Introduce yourself in a few words",
    stream= True
)

for event in stream: 
    print(event) 