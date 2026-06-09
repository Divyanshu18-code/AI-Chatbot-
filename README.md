# AI Chatbot Agent 🤖

An AI-powered chatbot agent built with **LangGraph**, **Groq**, **FastAPI**, and **Streamlit**. The agent supports real-time web search via Tavily and runs blazing-fast inference using Groq's free LLMs.

---

## Features

- React-style AI agent using LangGraph's `create_react_agent`
- Groq LLMs for fast inference (`llama-3.3-70b-versatile`, `llama-3.1-8b-instant`)
- Optional real-time web search powered by Tavily
- FastAPI REST backend with Pydantic schema validation
- Clean and simple Streamlit frontend UI
- Custom system prompt — define your agent's personality

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Agent Orchestration | LangGraph |
| LLM Provider | Groq |
| Web Search | Tavily |
| Backend | FastAPI + Uvicorn |
| Frontend | Streamlit |
| Language | Python 3.10+ |

---

## Project Structure

```
chatbot/
├── ai_agent.py      # LangGraph agent setup & LLM logic
├── backend.py       # FastAPI server (REST API)
├── frontend.py      # Streamlit UI
└── README.md
```

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Divyanshu18-code/AI-Chatbot-.git
cd AI-Chatbot-
```

### 2. Create and activate a virtual environment

```bash
pip install pipenv
pipenv shell
```

### 3. Install dependencies

```bash
pip install langchain-groq langchain-tavily langgraph fastapi uvicorn streamlit
```

### 4. Set your API keys


```bash
set GROQ_API_KEY=your_groq_api_key
set TAVILY_API_KEY=your_tavily_api_key
```




---

## Running the App

### Step 1 — Start the backend (Terminal 1)

```bash
python backend.py
```

You should see:
```
Uvicorn running on http://127.0.0.1:9999
```

### Step 2 — Start the frontend (Terminal 2)

```bash
streamlit run frontend.py
```

The app will open automatically at `http://localhost:8501`

---

## How It Works

```
User Query (Streamlit UI)
        ↓
FastAPI Backend (/chat endpoint)
        ↓
LangGraph Agent (create_react_agent)
        ↓
Groq LLM  ←→  Tavily Web Search (optional)
        ↓
AI Response → Streamlit UI
```

---

## Available Models

| Model | Provider | Speed |
|-------|----------|-------|
| llama-3.3-70b-versatile | Groq | Fast |
| llama-3.1-8b-instant | Groq | Fastest |

---

## API Reference

### `POST /chat`

**Request body:**
```json
{
  "model_name": "llama-3.3-70b-versatile",
  "system_prompt": "Act as a helpful assistant",
  "messages": ["What is the capital of France?"],
  "allow_search": false
}
```

**Response:**
```json
"The capital of France is Paris."
```
