from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

from data_loader import load_documents, split_documents


# PubMedBERT — medical-domain embedding model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Load and split documents
docs = load_documents()
chunks = split_documents(docs)

# Store in ChromaDB (persisted to disk)
vectordb = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="./chroma_db"
)

# Save database to disk
vectordb.persist()

print(f"✅ Stored {len(chunks)} chunks in ChromaDB")