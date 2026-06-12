from langchain_community.document_loaders import PyPDFLoader, CSVLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os

def load_documents(data_folder="data/"):
    docs = []
    for f in os.listdir(data_folder):
        path = os.path.join(data_folder, f)
        if f.endswith(".pdf"):
            loader = PyPDFLoader(path)
            docs.extend(loader.load())
        elif f.endswith(".csv"):
            loader = CSVLoader(path, encoding="utf-8")
            docs.extend(loader.load())
    return docs

def split_documents(docs):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    return splitter.split_documents(docs)