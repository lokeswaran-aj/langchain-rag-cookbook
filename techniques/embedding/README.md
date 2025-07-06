# Embedding

Embedding is the process of converting text into a vector of numbers. This is useful for similarity search.

## Why it is useful?

- LLMs are good with numbers, but not with text.
- Embedding is used to find the similarity between two texts.

## What are the different types of embedding?

### [HyDE (Hypothetical Document Embeddings)](./hyde-embedding.ipynb)

HyDE is an innovative retrieval technique that transforms user queries into hypothetical answer documents before performing similarity search. Rather than directly embedding a question, HyDE uses an LLM to generate a synthetic document that could plausibly answer that question. The key insight is that comparing document embeddings to document embeddings (rather than question embeddings to document embeddings) leads to more semantically meaningful similarity scores. By projecting queries into the same distributional space as the target documents, HyDE helps overcome the inherent mismatch between questions and answers in traditional embedding-based retrieval systems. This approach has been shown to significantly improve retrieval accuracy compared to direct query embedding.
