# Common-Sense Guide to AI Engineering

A practical Python learning project based on *A Common-Sense Guide to AI Engineering* by Jay Wengrow.

The goal of this repository is to learn AI Engineering by writing code, running experiments, understanding Large Language Models (LLMs), and building practical AI applications.

## Learning Environment

- **Computer:** Apple Mac M1
- **Language:** Python
- **Local LLM runtime:** Ollama
- **Model:** Qwen3.5:4B
- **Development environment:** PyCharm

I aim to run local LLM experiments wherever practical and understand the underlying Python code rather than relying only on graphical tools.

## Project Structure

```text
common_sense_guide_to_ai_engineering/
├── README.md
├── chp1/
│   ├── chp1_chatbot_1.py
│   └── chp1_chatbot_2.py
├── chp2/
└── chp3/
```

Each chapter has its own folder to keep the code and experiments organized.

## Chapter 1: Getting Started with LLMs

### Experiment 1 — First Chatbot

File: `chp1/chp1_chatbot_1.py`

- Send a question to Qwen3.5:4B using Ollama.
- Inspect the model's response.
- Check the generation finish reason.
- Investigate unexpected response times and output quality.

### Experiment 2 — Improving the Chatbot

File: `chp1/chp1_chatbot_2.py`

- Write a more specific prompt.
- Experiment with `think=False` when supported by the model.
- Set `num_predict` to limit generated tokens.
- Inspect `response.done_reason`.
- Compare the output with the first experiment.

These experiments explore how prompt design and model configuration can affect the behavior of a local LLM.

## Chapters 2 and 3

The `chp2/` and `chp3/` folders are reserved for code and experiments as I progress through the book.

I will add scripts, practical exercises, and notes as the project develops.

## Setup

### 1. Install Ollama

Download Ollama from:

https://ollama.com/

### 2. Download the model

Open a terminal and run:

```bash
ollama pull qwen3.5:4b
```

### 3. Install the Python package

Activate your project's Python virtual environment, then run:

```bash
python -m pip install ollama
```

### 4. Run a Chapter 1 experiment

From the project root, run:

```bash
python chp1/chp5_chatbot_1.py
```

Or run the improved version:

```bash
python chp1/chp5_chatbot_2.py
```

Make sure Ollama is installed, the model is available locally, and the Ollama service is running.

## Learning Approach

For each experiment, I aim to:

1. Understand the problem and the expected result.
2. Write and run the Python code.
3. Observe the model's behavior.
4. Investigate unexpected results.
5. Change one or more settings and compare the outcomes.
6. Record what I learn.

The emphasis is on practical experimentation, understanding the code, and developing the skills needed to build AI applications.

## Progress

- [x] Create the project structure.
- [x] Run the first local LLM experiment.
- [x] Improve the prompt and experiment with generation settings.
- [ ] Continue with Chapter 2.
- [ ] Continue with Chapter 3.
- [ ] Build more practical AI applications.

## Reference

Wengrow, Jay. *A Common-Sense Guide to AI Engineering.*

This repository contains my own learning code and experiments inspired by the book. It is a work in progress.
