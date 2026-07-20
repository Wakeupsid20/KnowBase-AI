from app.services.embedding_service import (
    chunk_text,
    generate_embeddings,
)

sample = """
Artificial Intelligence is transforming industries.
Machine Learning enables systems to learn from data.
Deep Learning is a subset of Machine Learning.
"""

chunks = chunk_text(sample)

embeddings = generate_embeddings(chunks)

print("Number of chunks:", len(chunks))
print("Embedding shape:", embeddings.shape)
print("First embedding (first 10 values):")
print(embeddings[0][:10])