# Experiment 1: My first attempt

from ollama import chat

response = chat(
    model="qwen3.5:4b",
    messages=[
        {
            "role": "user",
            "content": (
                "What Alan Turing contribute to the Computer Science"
            )
        }
    ],
    options={
        "temperature": 0,
    }
)

print(response.message.content)