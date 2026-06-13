# 🩺 CliniqBot

> A RAG-powered clinical assistant that helps with patient triage and symptom analysis using real medical data.

Built as part of the **AI-Enabled Healthcare for Industrial Readiness** workshop — combining everything from signal processing fundamentals to LLM-based generative AI into one working clinical assistant.

---

## 💡 What it does

CliniqBot takes a patient's described symptoms and:

- 🔍 Searches through thousands of real clinical notes (MTSamples + ChatDoctor datasets) to find relevant medical context
- 🧠 Uses an LLM (Llama 3.3 via Groq) to generate a grounded, context-aware response
- 🚨 Flags emergency symptoms instantly with a triage layer — before the AI even responds
- 🛡️ Always recommends consulting a real doctor — built with safety as a priority, not an afterthought

It's not trying to replace a doctor. It's trying to be the first, fast, informative step before you see one.

---

## 🖥️ See it in action

Ask it something like:

> "I have throat pain like a stone got stuck in my throat, and a cold"

And it'll come back with a proper differential — common cold, strep throat, tonsillitis — pulled from real clinical data, along with a recommendation to see a doctor.

---

## ⚙️ Tech stack

| Layer | Tool |
|---|---|
| LLM | Llama 3.3 (via Groq API) |
| RAG framework | LangChain |
| Vector database | ChromaDB |
| Embeddings | `sentence-transformers/all-MiniLM-L6-v2` |
| Frontend | Streamlit |
| Datasets | MTSamples + ChatDoctor |

---

## 🚀 Running it locally


# clone the repo
git clone https://github.com/Sajan-2/CliniqBot.git
cd CliniqBot

# set up virtual environment
py -m venv venv
venv\Scripts\activate

# install dependencies
pip install -r requirements.txt

# add your Groq API key
echo GROQ_API_KEY=your_key_here > .env

# build the vector database (takes 10-15 mins first time)
py ingest.py

# run the app
streamlit run app.py
```

---

## 📁 Project structure

```
CliniqBot/
├── data/             → clinical datasets (MTSamples, ChatDoctor)
├── chroma_db/        → vector database (auto-generated, not in repo)
├── data_loader.py    → loads & chunks documents
├── ingest.py         → embeds and stores chunks in ChromaDB
├── rag_chain.py       → core RAG pipeline (retrieval + LLM)
├── triage.py         → emergency keyword detection
├── app.py            → Streamlit chat interface
├── requirements.txt
└── .env              → API key (not in repo)
```

---

## 🧠 How it works

```
User describes symptoms
        ↓
Triage check (emergency keywords?)
        ↓
ChromaDB retrieves relevant clinical notes
        ↓
LLM generates response grounded in retrieved context
        ↓
Response shown with safety disclaimer
```

---

## ⚠️ Disclaimer

CliniqBot is built for educational and demonstration purposes as part of a workshop project. It is **not a medical device** and should never be used as a substitute for professional medical advice, diagnosis, or treatment. Always consult a qualified healthcare provider for any health concerns.

---

## 🙋 About this project

This was built solo from scratch as a group project for the AI-Enabled Healthcare for Industrial Readiness workshop — going from zero RAG knowledge to a working end-to-end clinical AI assistant, including all the debugging, version conflicts, and "why is this not working" moments along the way 😅

If you're checking this out and have questions about how any part of it works, feel free to open an issue!
