# install libraries we need these
!pip install transformers
!pip install torch
!pip install nltk
!pip install sumy
!pip install PyMuPDF

# importing stuff
from transformers import pipeline
import nltk
nltk.download('punkt')
nltk.download('punkt_tab') # Download punkt_tab as well
import fitz  # pdf reader
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from google.colab import files

# loading that bart summarizer thing from huggingface
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# i made this function to do the summarizing with bart
def do_summary_bart(bigtext):
    out = summarizer(bigtext, max_length=130, min_length=30, do_sample=False)
    return out[0]['summary_text']

# this one is for that LSA thing someone on yt said is good
def do_summary_lsa(text, num_sentences=4):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    lsa = LsaSummarizer()
    summ = lsa(parser.document, num_sentences)
    return " ".join(str(s) for s in summ)

# i wrote this to read txt files
def read_txt(f):
    with open(f, 'r', encoding='utf-8') as file:
        return file.read()

# this works for pdfs i think
def read_pdf(f):
    doc = fitz.open(f)
    text = ''
    for pg in doc:
        text += pg.get_text()
    return text

# upload the file
print("upload a file please  (.txt or .pdf)")
uploaded = files.upload()

fname = list(uploaded.keys())[0]  # getting file name

# figuring out what type it is
if fname.endswith('.txt'):
    fulltext = read_txt(fname)
elif fname.endswith('.pdf'):
    fulltext = read_pdf(fname)
else:
    print("not supported file bro")

# asking what summary style
print("Pick one:")
print("1 - fancy BART AI model")
print("2 - LSA old school extractive method")

choice = input("what u want (1/2): ")

if choice == '1':
    result = do_summary_bart(fulltext)
    print("\nHere is your fancy AI summary:\n")
    print(result)
elif choice == '2':
    result = do_summary_lsa(fulltext)
    print("\nOld school LSA summary:\n")
    print(result)
else:
    print("idk what you typed 🤷‍♂️")

# also showing the real text first 1000 chars
print("\n----- Original article (first part) -----\n")
print(fulltext[:1000])

# and showing the final thing again
print("\n----- Final Summary Below -----\n")
print(result)
