import ollama
import os

model = "mistral"
ollama_host = os.getenv("OLLAMA_HOST", "http://localhost:11434")

# Set the Ollama host (important when using Docker)
ollama.base_url = ollama_host

messages = [
    {"role": "system", "content": "You are an expert computer engineering professor named Kit."}
]

print("👋 Hello, my name is Kit Bot")

while True:
    content = input("> Enter message: ")
    if content.lower() == "kill":
        print("👋 Goodbye")
        break

    print("...")
    messages.append({"role": "user", "content": content})

    response = ollama.chat(
        model=model,
        messages=messages
    )

    kit_response = response['message']['content']
    print("Kit Bot:", kit_response + "\n")

    messages.append({"role": "assistant", "content": kit_response})
