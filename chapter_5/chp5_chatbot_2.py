# Experiment 2: Improving the prompt and model configuration

from ollama import chat

response = chat(
    model="qwen3.5:4b",
    messages=[
        {
            "role": "user",
            "content": (
                "What are Alan Turing's three most important "
                "contributions to computer science? "
                "Explain each in one short sentence. "
                "Use a numbered list."
            )
        }
    ],
    think=False,
    options={
        "temperature": 0,
        "num_predict": 250
    }
)

print(response.message.content)
print("Finish reason:", response.done_reason)