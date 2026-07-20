from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer

# Load once when the application starts
model = SentenceTransformer("all-MiniLM-L6-v2")


def chunk_text(text: str):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100,
    )
    return splitter.split_text(text)


def generate_embeddings(chunks: list[str]):
    return model.encode(chunks, convert_to_numpy=True)