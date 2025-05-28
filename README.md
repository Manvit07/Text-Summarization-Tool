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

## Screen Shot 

![Image](https://github.com/user-attachments/assets/94a58b55-460f-437a-885a-254cd85ae9ab)
![Image](https://github.com/user-attachments/assets/d409b113-9767-4de5-b9d6-7749d93359ff)
![Image](https://github.com/user-attachments/assets/4e2a4d86-4bde-4a6c-850e-12b1b5e5bc91)
![Image](https://github.com/user-attachments/assets/fe3de281-69c5-4977-9c6c-33e0f63dc853)
![Image](https://github.com/user-attachments/assets/1d58438a-121f-436a-9c82-c671d9a05bd5)
![Image](https://github.com/user-attachments/assets/683bd599-cbff-4a8f-85fa-696a2a4faaf4)
![Image](https://github.com/user-attachments/assets/0d0a68cb-3be3-4a85-ba87-f0c57cb58c23)
![Image](https://github.com/user-attachments/assets/635f25c7-1b8e-47d9-b9c8-3f1b53ae2ced)

## 📝 Notes

- BART summarization works better for natural English and long paragraphs. LSA is faster and more interpretable.
- This tool runs fine for **texts up to 1,000–1,500 words**. For longer ones, you might need to chunk the input (future improvement idea).
- I intentionally kept the code a little messy to look like a real beginner wrote it (because I am one 😅). But it still works!

---
