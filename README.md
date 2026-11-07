#  Local LLM Chatbot Using LangChain Memory

##  Project Overview

This project is a simple AI chatbot built using a Local Large Language Model (LLM), Ollama, LangChain, and Streamlit.

The chatbot can communicate with users, answer questions, and remember previous conversations using LangChain Memory.

It runs locally on the computer using the Llama 3.2 model.

##  Objectives

- To build a simple AI chatbot.
- To use a Local LLM through Ollama.
- To integrate LangChain for conversation management.
- To implement conversation memory.
- To create an interactive chatbot interface using Streamlit.

##  Technologies Used

- Python
- Ollama
- Llama 3.2
- LangChain
- Streamlit

##  Project Structure

```text
Local-LLM-Chatbot/
│
├── app.py
├── requirements.txt
└── README.md
```

## Application Preview
<img width="1348" height="599" alt="image" src="https://github.com/user-attachments/assets/539d23e4-8b83-487f-a47b-1a7d1b360884" />
<img width="1348" height="607" alt="image" src="https://github.com/user-attachments/assets/2bcde48c-3a52-4b4d-8c86-c4348a6064b2" />



##  Installation and Setup

### Step 1: Install Python

Download and install Python from:

https://www.python.org/downloads/

### Step 2: Install Ollama

Download Ollama from:

https://ollama.com/download

### Step 3: Download Llama 3.2

Open the terminal and execute:

```bash
ollama pull llama3.2
```

### Step 4: Clone the Repository

```bash
https://github.com/nikithanka7-byte/Local-LLM-Chatbot
```

### Step 5: Navigate to Project Folder

```bash
cd Local-LLM-Chatbot
```

### Step 6: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 7: Run the Application

```bash
streamlit run app.py
```

The chatbot will open in your default web browser.

##  Example Conversation

**User:**
Hello, my name is Nikitha.

**AI Chatbot:**
Hello Nikitha! Nice to meet you.

**User:**
What is my name?

**AI Chatbot:**
Your name is Nikitha.

The chatbot remembers previous messages using LangChain conversation history.

##  Key Features

1. Local AI Chatbot.
2. Llama 3.2 Language Model.
3. Conversation Memory.
4. Context-aware responses.
5. Interactive Streamlit Interface.
6. Chat History Management.
7. Clear Chat Option.

##  Working Process

1. User enters a message.
2. Streamlit receives the input.
3. LangChain processes the conversation.
4. Ollama sends the input to the local Llama 3.2 model.
5. The model generates a response.
6. LangChain stores the conversation history.
7. The chatbot displays the response.

## Future Enhancements

- Add voice input and output.
- Support multiple LLM models.
- Save chat history permanently.
- Add file upload functionality.
- Improve chatbot interface.

## Conclusion

This project demonstrates how to develop an AI chatbot using a Local LLM with LangChain Memory. Ollama runs the language model locally, LangChain manages conversation history, and Streamlit provides an interactive user interface.

The chatbot can remember previous messages and generate meaningful responses.

## Author

**Nikitha R.**

B.Sc. Computer Science with Artificial Intelligence
