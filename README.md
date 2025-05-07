### VaaniNews - News Summarization, Sentiment Analysis & Hindi Text-to-Speech Application

## 🧠 Overview
**VaaniNews** is a full-stack NLP application that summarizes news articles about a company, analyzes their sentiment, and generates a Hindi audio output of the summary. It integrates **Gemini-Flash** for summarization, **LLaMA-2 via LangChain-Groq** for sentiment analysis, and **Google Cloud Text-to-Speech** for multilingual speech generation.

Users input a company name and receive:
- Summarized news content
- Sentiment insights (Positive/Neutral/Negative)
- Hindi speech output
- Evaluation metrics

---

## ⚙️ Installation & Setup

### 📋 Prerequisites
- Python 3.8+
- Google Cloud credentials (TTS + Translate)
- Groq API Key (for LangChain-Groq)
- EventRegistry API Key (or your own news source)

### 🛠 Installation Steps

1. **Clone the repository**:
```bash
git clone https://github.com/yourusername/NLP_Project_VaaniNews.git
cd NLP_Project_VaaniNews
````

2. **Create and activate a virtual environment**:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install the dependencies**:

```bash
pip install -r requirements.txt
```

4. **Set up environment variables**:
   Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
GOOGLE_APPLICATION_CREDENTIALS=./path-to-your-google-credentials.json
EVENT_REGISTRY_API_KEY=your_event_registry_key
```

---

## 🤖 Model Components

### 📄 Summarization Model

* **Gemini-2.0-Flash** generates concise, context-rich summaries from news text.
* TF-IDF is used to select the most relevant sentences before summarization.

### 💬 Sentiment Analysis Model

* Uses **LangChain + Groq** with **LLaMA-2** for zero-shot sentiment classification.
* Labels include: `Positive`, `Neutral`, and `Negative`.

### 🔊 Text-to-Speech (TTS) Model

* Translates final summary into Hindi using Google Translate API.
* Uses **Google Cloud Text-to-Speech** to synthesize Hindi speech (MP3 format).

---

## 🔌 API Development

The backend is powered by **FastAPI** and handles news processing, summarization, sentiment analysis, translation, and TTS generation.

### 📡 API Endpoints

#### 🔍 1. Fetch News & Analyze Sentiment

```http
GET /fetch_news?company=Zomato
```

Returns summarized articles, sentiment, and audio.

#### 🌐 2. Translate Text to Hindi

```http
GET /translate?text=Your Text&target_language=hi
```

#### 🔊 3. Generate TTS from Text

```http
GET /generate_tts?text=Your Hindi Text
```

---

## 🧪 Evaluation Metrics

| Metric   | Description               |
| -------- | ------------------------- |
| **CRS**  | Company Relevance Score   |
| **SPS**  | Summary Precision Score   |
| **FCS**  | Factual Consistency Score |
| **SAS**  | Sentiment Agreement Score |
| **HR**   | Hallucination Rate        |
| **CR**   | Compression Ratio         |
| **COVS** | Coverage Score            |

All are computed over a 50-row curated dataset.

---

## 📦 Example Output - Zomato

**Input**: `Zomato`

**Output Includes**:

* 10 Zomato-related news articles
* Summaries via Gemini-Flash
* Sentiment labels (e.g., 6 Neutral, 3 Positive, 1 Negative)
* Final Summary
* Hindi audio output (MP3)

**Output**:
[![VaaniNews Output]]
(https://github.com/user-attachments/assets/3804b347-fcc4-48b3-9df0-402564d7fc29)



---

## 🧪 Testing with Postman

1. Run FastAPI backend:

```bash
uvicorn api:app --reload
```

2. Use Postman to test endpoints like:

```
http://127.0.0.1:8000/fetch_news?company=Zomato
```

---

## ⚠️ Assumptions & Limitations

* Scraping is limited to static (non-JS) sources.
* Sentiment is zero-shot and may lack nuance in edge cases.
* Google Cloud APIs require active credentials.
* Hindi is the only supported language for audio output currently.

---

## 🚀 Running the Application

### Start Backend (FastAPI)

```bash
uvicorn api:app --reload
```

### Start Frontend (Streamlit)

```bash
streamlit run app.py
```

---

## 📚 Citation

If you use or extend this project, cite as:

```
@project{vaaninews2025,
  title={VaaniNews: A Multilingual Pipeline for Company News Summarization, Sentiment Analysis, and Speech Delivery},
  author={Jeet Choksi, Tanay Shukla},
  year={2025},
  note={University of Colorado Boulder, NLP Class Project}
}
```

---

## 💡 Future Enhancements

* Add multilingual TTS (Mandarin, Spanish)
* Fine-tune sentiment model on financial corpora
* Detect real-time sentiment drift
* Host on Hugging Face Spaces or Streamlit Cloud
