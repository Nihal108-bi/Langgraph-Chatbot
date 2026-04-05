
## 🤖 LangGraph: Build Stateful Agentic AI Graph

This project is an end-to-end Agentic AI application that leverages **LangGraph** to create stateful, multi-turn conversational agents. It features multiple use cases, including a basic chatbot, a web-enabled research assistant, and an automated AI news aggregator.

### 🌟 Key Features
* **Stateful Orchestration**: Uses LangGraph to manage conversation state and complex node transitions.
* **Real-time Streaming**: Implements token-by-token streaming for a dynamic "typing" effect in the UI.
* **Web Integration**: Integrated with **Tavily Search** for real-time internet access and factual grounding.
* **Multiple Use Cases**: 
    * **Basic Chatbot**: Direct LLM interaction.
    * **Chatbot with Web**: Agentic loop that decides when to use tools.
    * **AI News Explorer**: Fetches and summarizes the latest AI news into structured Markdown.
* **Interactive UI**: Built with Streamlit, supporting model configuration and API key management.

---

## 🏗️ Graph Structure & Architecture

The application uses a directed graph approach to manage the logic flow for different use cases.

### 1. Basic Chatbot
A simple linear flow where the user input is processed by the LLM and returned.
`START` ➔ `Chatbot Node` ➔ `END`

### 2. Chatbot with Web (Agentic Loop)
An advanced loop where the LLM can call external tools.
* **START**: The process begins with user input.
* **Chatbot Node**: The LLM decides if it needs to search the web based on the query.
* **Conditional Edge**: 
    * If a **Tool Call** is required ➔ `Tools Node`.
    * If the answer is ready ➔ `END`.
* **Tools Node**: Executes the Tavily Search and sends results back to the `Chatbot Node` for final synthesis.

### 3. AI News Explorer
A sequential pipeline for automated data processing.
`START` ➔ `Fetch News` ➔ `Summarize News` ➔ `Save Result` ➔ `END`

---

## 🛠️ Tech Stack
* **Framework**: LangGraph, LangChain
* **LLM Interface**: Groq (supports Llama 3.1, etc.)
* **Search Engine**: Tavily API
* **UI Framework**: Streamlit
* **Language**: Python 3.13

---

## 🚀 Getting Started

### 1. Installation
Clone the repository and install the dependencies:
```bash
git clone https://github.com/Nihal108-bi/Langgraph-Chatbot
cd langgraph-chatbot
pip install -r requirements.txt
```

### 2. Configuration
The application uses an `.ini` file for UI settings and environment variables for API keys.
* **Config**: Located at `src/langgraphagenticai/ui/uiconfigfile.ini`.
* **Keys**: You will need a **Groq API Key** and a **Tavily API Key** (entered directly in the Streamlit sidebar).

### 3. Running the App
```bash
streamlit run app.py
```

---

## 📁 Project Directory
* `src/langgraphagenticai/nodes/`: Contains the logic for each graph node (Chat, News, Tools).
* `src/langgraphagenticai/graph/`: Defines the `GraphBuilder` and routing logic.
* `src/langgraphagenticai/ui/`: Streamlit interface and configuration files.
* `src/langgraphagenticai/LLMS/`: LLM configuration (Groq integration).