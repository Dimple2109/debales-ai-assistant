# 🚀 Debales AI Assistant (LangGraph + RAG + Gemini)

An intelligent AI assistant that answers questions using both internal knowledge (RAG) and real-time web search (SERP API). Built using LangGraph for workflow orchestration and Google Gemini for response generation.

---

## 📌 Features

- 🔍 Website scraping (Debales AI content)
- 🧠 Retrieval-Augmented Generation (RAG)
- 🌐 SERP API integration for external queries
- 🔀 Smart routing using LangGraph
- 🤖 Gemini-powered responses
- 💻 CLI-based chatbot interface
- ⚡ Fast and lightweight architecture

---

## 🏗️ Tech Stack

- Python 3.10+
- LangGraph
- LangChain
- Google GenAI (Gemini API)
- HuggingFace Embeddings
- FAISS (Vector Database)
- BeautifulSoup + Requests

---

## 📁 Project Structure

```
debales_ai_agent/
│
├── app.py                # Main entry point (CLI chatbot)
├── agent_flow.py         # LangGraph workflow logic
├── llm_client.py         # Gemini API integration
├── scraper_engine.py     # Website scraping module
├── vector_engine.py      # RAG + FAISS vector store
├── search_tool.py        # SERP API integration
├── config.py             # Environment config loader
├── schema.py             # State schema definition
├── requirements.txt      # Dependencies
└── .env                  # API keys (not included in repo)
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone <your-repo-link>
cd debales_ai_agent
```

---

### 2️⃣ Create Virtual Environment (Optional)

```bash
python -m venv venv
```

Activate:

**Windows**
```bash
venv\Scripts\activate
```

**Mac/Linux**
```bash
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Add API Keys

Create a `.env` file:

```
GOOGLE_API_KEY=your_google_api_key
SERP_API_KEY=your_serp_api_key
```

---

## ▶️ Run the Project

```bash
python app.py
```

---

## 💬 Example Usage

```
You: What is Debales AI?
Bot: (Answer from knowledge base using RAG)

You: Latest AI news
Bot: (Answer using SERP API + Gemini)
```

---

## 🧠 How It Works

```
User Query
   ↓
LangGraph Router
   ↓
 ┌───────────────┬───────────────┐
 │               │               │
RAG         SERP API       (Mixed possible)
 │               │
 └──────→ Gemini LLM ←────┘
           ↓
     Final Answer
```

---

## ⚠️ Important Notes

- Ensure valid API keys are set in `.env`
- Recommended model: `gemini-2.5-flash` or fallback `1.5-flash`
- First run may take time due to scraping & embedding
- Internet connection required for SERP API

---

## 🚀 Future Improvements

- 🌐 Web UI (Streamlit / React)
- 🧠 Chat memory (conversation history)
- ⚡ Streaming responses
- 🔌 Multi-tool agent support
- 🚀 FastAPI backend deployment

---

## 📦 Submission Includes

- ✅ Source Code
- ✅ README.md
- ✅ `.env`
- ✅ Demo Video
- ✅ Sample Inputs & Outputs

---

## 👨‍💻 Author

Dimple Vasita

---

## ⭐ Notes

This project demonstrates:
- RAG implementation
- Tool calling (SERP API)
- LangGraph workflow design
- Real-world AI assistant architecture