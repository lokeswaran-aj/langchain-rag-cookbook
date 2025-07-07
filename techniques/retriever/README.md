# Retriever

Retriever is a component that retrieves relevant documents from a vector store.

## What are the different types of retrievers?

### [Vector Store Retriever](./vector-store-retriever.ipynb)

A vector store retriever is a retriever that uses a vector store to retrieve documents. It is a lightweight wrapper around the vector store class to make it conform to the retriever interface. It uses the search methods implemented by a vector store, like similarity search and MMR, to query the texts in the vector store.

### [BM25 Retriever](./bm25-retriever.ipynb)

BM25 Retriever is a retriever that uses the Okapi BM25 ranking algorithm to retrieve documents. BM25 (Best Matching) is a ranking function used by search engines to estimate the relevance of documents to a given search query. It scores and ranks documents based on the search terms appearing in each document, regardless of their proximity within the document.
