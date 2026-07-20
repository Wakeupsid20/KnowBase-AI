from app.services.embedding_service import chunk_text

sample = """
Artificial Intelligence is transforming industries worldwide.
Machine learning allows computers to learn from data.
Deep learning is a subset of machine learning.
"""

chunks = chunk_text(sample)

for i, chunk in enumerate(chunks, start=1):
    print(f"\nChunk {i}\n{'-'*30}")
    print(chunk)