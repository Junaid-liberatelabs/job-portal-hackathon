from fastembed import TextEmbedding
documents = [
    "FastEmbed is lighter than Transformers & Sentence-Transformers.",
    "FastEmbed is supported by and maintained by Qdrant.",
]
embedding_model = TextEmbedding()
embeddings_generator = embedding_model.embed(documents)
embeddings_list = list(embeddings_generator)
print(embeddings_list)