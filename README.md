# 🧠 Hybrid Log Classification System

A smart log classification system that combines three different techniques to maximize accuracy and efficiency:

- **Regex-based Matching** (Fastest)
- **BERT-based Classification** (for moderately available data)
- **LLM-based Classification using DeepSeek R1** (for low-sample scenarios)

Built using **FastAPI** and served with **Uvicorn**, this project is designed for real-time log analysis and classification.

---

## 🏗️ Architecture

```mermaid
                      ┌────────────┐
                      │   Client   │
                      └────┬───────┘
                           │
              HTTP Request │
                           ▼
               ┌─────────────────────┐
               │  FastAPI + Uvicorn  │
               └────┬──────┬─────────┘
                    │      │
                    ▼      ▼
         ┌──────────────────┐
         │ Regex Pattern DB │◄─────────────┐
         └────────┬─────────┘              │
                  │  Match?                │
        ┌─────────▼──────────┐             │
        │  Regex Classifier  │             │
        └─────────┬──────────┘             │
                  │ Yes                   No
                  ▼                        │
            Return Result         ┌────────▼────────┐
                                  │ Enough Samples? │
                                  └─────┬─────▲─────┘
                                       │     │
                                    Yes│     │No
                                       ▼     ▼
                    ┌─────────────────────────────┐
                    │ BERT Embedding + Logistic   │
                    │ Regression (Sklearn Model)  │
                    └────────────┬────────────────┘
                                 │
                      ┌──────────▼─────────────┐
                      │   DeepSeek R1 LLM via  │
                      │   Groq API (Fallback)  │
                      └──────────┬─────────────┘
                                 │
                          ┌──────▼───────┐
                          │ Final Result │
                          └──────────────┘

```

> Replace this with a visual diagram if preferred.

---

## 🔧 Tech Stack

- **FastAPI**: Web API
- **Uvicorn**: ASGI server
- **Regex**: First-pass filter
- **BERT (Sentence-Transformers)**: Embedding generation
- **Scikit-learn**: Logistic Regression classifier
- **DeepSeek R1 (via Groq)**: LLM-based fallback classification
- **Python-Dotenv**: Environment variable management
- **Joblib**: Model persistence

---

## 📦 Requirements

Install all dependencies with:

```bash
pip install -r requirements.txt
```

**requirements.txt**
```
fastapi
uvicorn
python-dotenv
groq
sentence-transformers
joblib
pandas
scikit-learn
```

---

## 🚀 Running the Server

```bash
uvicorn server:app --reload
```
---

## 🧪 Example Usage

Make a POST request to `/classify`:

---

## 📁 Project Structure

```
.
├── models/
│   └── log_classifier.joblib
├── resources/
│   └── test.csv
├── training/
│   └── dataset
        └── synthetic_logs.csv
    └── training.ipynb
├── .env
├── classify.py
├── processor_bert.py
├── processor_llm.py
├── processor_regex.py
├── requirements.txt
└── README.md
├── server.py
```

---

## 🔐 Environment Variables

Create a `.env` file with the following:

```
GROQ_API_KEY=your_groq_api_key
```

---

## ✍️ Author

- **Madhuka Abhishek**
- Open to feedback and collaboration!

---

## 📜 License

This project is licensed under the MIT License. See the `LICENSE` file for details.

