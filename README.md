# Text-Summarization-Tool

# INTERACTIVE-QUIZ-APPLICATION

*COMPANY*: CODTECH IT SOLUTIONS PVT.LTD

*NAME*: Manvit Mahesh Deshmukh

*INTERN ID*: CT12DL764

*DOMAIN*: Artificial intelligence.

*DURATION*: 12 weeks

*MENTOR*:  Neela Santhosh Kumar


# 📄 Text Summarization Tool Using NLP

## ✨ Project Title: **Text Summarization Tool Using NLP**

---

## 🧠 Description

A project to automatically summarize long articles or text documents. The idea is simple: you upload a long `.txt` or `.pdf` file (like news, Wikipedia articles, essays, etc.) and the code gives you a short and clean summary. This project uses Natural Language Processing (NLP) to make reading long stuff easier.

I used two main methods for summarizing:
1. **BART (abstractive summarization)** – a fancy deep learning model from Hugging Face that tries to *understand and rewrite* the content like a human would.
2. **LSA (extractive summarization)** – a more traditional statistical method using the Sumy library that just *picks out the most important sentences*.

Both work fine, and I added an option to choose whichever one you want when you run the notebook.

---

## 💻 How to Use (for anyone)

### Step-by-step:

1. Open the notebook in **Google Colab** (easiest way, no setup needed).
2. Run the first cell to **install required packages** like `transformers`, `sumy`, `nltk`, etc.
3. Upload a `.txt` or `.pdf` file when prompted.
4. The tool will detect the file type and extract the text from it.
5. You’ll be asked to pick a summarization model:
    - Type `1` for BART (uses AI model, more accurate)
    - Type `2` for LSA (fast and simple)
6. The summary will be printed, along with a snippet of the original text for comparison.

### Example:
You upload a 10-page PDF of a news article → pick `BART` → it shows a 3-4 line summary of the whole thing.

---

## 🧰 Libraries/Tech Used

- `transformers` – for the BART model (`facebook/bart-large-cnn`)
- `sumy` – for LSA summarization
- `PyMuPDF` – to read `.pdf` files
- `nltk` – for tokenization (used by Sumy)
- `Google Colab` – to run everything in the browser
- `pydub` – optional, if you expand with audio later

---

