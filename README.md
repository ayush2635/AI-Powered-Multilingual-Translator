# 🌍 AI-Powered Multilingual Translator 🔁🧠

> 🚀 A powerful multilingual text translator built using **mBART50** from Facebook AI, fine-tuned on high-quality open datasets from **OPUS Books** and **IIT Bombay**.  
> 🌐 Supports translations between **English ↔ Spanish, French, Italian, Portuguese, and Hindi**.

---

## 📸 Demo Screenshot

![App Screenshot](https://raw.githubusercontent.com/ayush2635/AI-Powered-Multilingual-Translator/main/assets/screenshot.png)

---

## ✨ Features

- 🔁 Translate between 5+ languages using mBART50
- 📚 Trained on OPUS Books and IIT Bombay English-Hindi corpora
- ⚡ Fast & light inference
- 🧠 Powered by 🤗 Transformers, PyTorch
- 🌐 Clean and easy-to-use Streamlit web UI

---

## 🧠 Model Details

- **Base Model**: [`facebook/mbart-large-50-many-to-many-mmt`](https://huggingface.co/facebook/mbart-large-50-many-to-many-mmt)
- **Fine-Tuned On**:
  - [`opus_books`](https://huggingface.co/datasets/opus_books) (en-es, en-fr, en-it, en-pt)
  - [`iitb_en_hi`](https://huggingface.co/datasets/iitb_en_hi) (en-hi)

---

## 🛠️ Tech Stack

| Tool         | Description                       |
|--------------|------------------------------------|
| 🤗 Transformers | Model loading & fine-tuning     |
| 🐍 PyTorch       | Deep learning backend           |
| 🧪 Hugging Face Datasets | Dataset provider         |
| 🌐 Streamlit    | Web frontend interface          |
| 🐙 GitHub       | Version control                 |

---

## 🚀 Getting Started (All-in-One Setup)

Follow these steps to set up and run the translator app on your local machine:

```bash
# 1. Clone the repository
git clone https://github.com/ayush2635/AI-Powered-Multilingual-Translator.git
cd AI-Powered-Multilingual-Translator

# 2. Create and activate a virtual environment
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the Streamlit app
streamlit run app.py
