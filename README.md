# 🧠 Local AI Restaurant Assistant using LangChain, Ollama, and RAG

This project demonstrates how to build a **local intelligent agent** using **LangChain**, **Ollama**, and **Retrieval-Augmented Generation (RAG)** to answer questions based on real restaurant reviews — all running **100% locally** without cloud APIs.

## 🍕 Use Case

The AI assistant acts as a smart interface for a pizza restaurant, capable of answering customer questions like:

> *"How are the vegan options?"*
> *"Is the restaurant good for families?"*
> *"How’s the service according to reviews?"*

It uses **vector embeddings**, **semantic search**, and a **local LLM** (`llama3.2`) to generate detailed, context-aware answers from realistic customer feedback.

---

## 🚀 Features

* 🔍 **RAG Pipeline** with `OllamaEmbeddings` + `ChromaDB`
* 🤖 **Locally hosted LLM** via `Ollama` (`llama3.2`)
* 📄 Parses and stores real review data with metadata (rating, date)
* ↺ Dynamically retrieves top 5 relevant reviews based on input query
* 💬 Command-line interface to ask questions and get rich natural language responses
* 🔒 Fully offline & privacy-preserving (no external API calls)

---

## 🧰 Tech Stack

* `Python`
* `LangChain`
* `Ollama`
* `Chroma` (Vector DB)
* `Pandas`
* `Retrieval-Augmented Generation (RAG)`

---

## 📂 Project Structure

```
📁 Resturant-review-project/
├── realistic_restaurant_reviews.csv     # Sample restaurant review data
├── vector.py                            # Embedding + Chroma vector store
├── main.py                              # Main app: input > retrieve > generate answer
├── app.py (optional UI)
└── README.md
```

---

## 📌 How to Run

1. **Install dependencies** (in a virtual environment):

```bash
pip install -r requirements.txt
```

2. **Start Ollama and make sure your models are available:**

```bash
ollama run llama3
```

3. **Run the app:**

```bash
python main.py
```

---

## 📊 Future Improvements

* Web UI (Gradio or Streamlit)
* User feedback loop (RLHF-style refinement)
* Multilingual review support
* Sentiment-aware answer generation

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).
