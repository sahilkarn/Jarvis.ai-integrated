from ollama import chat

response = chat(
    model="gemma3:4b",
    messages=[
        {
            "role": "user",
            "content": "Introduce yourself as JARVIS in one short paragraph."
        }
    ]
)

print(response.message.content)