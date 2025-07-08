# LangChain RAG Cookbook

This is a collection of notebooks that I used to learn about RAG with LangChain.

There are separate notebooks for each technique.

## Techniques

1. [Chunking](./techniques/chunking/README.md)
   Chunking is the process of splitting the document into smaller chunks so that it can be processed by the LLM. There are different techniques to chunk the document like [length-based](./techniques/chunking/length-based-chunking.ipynb), [text-based](./techniques/chunking/text-based-chunking.ipynb), [semantic-based](./techniques/chunking/semantic-based-chunking.ipynb), and [document-based](./techniques/chunking/document-based-chunking.ipynb).

2. [Query Rewriting](./techniques/query-rewriting/README.md)
   Query rewriting is the process of rewriting the query to make it more specific and relevant to the document. There are different techniques to rewrite the query like [multi-query](./techniques/query-rewriting/multi-query-rewriting.ipynb), [decomposition](./techniques/query-rewriting/decomposition-query-rewriting.ipynb) and [step-back](./techniques/query-rewriting/step-back-query-rewriting.ipynb)

3. [Embedding](./techniques/embedding/README.md)
   Embedding is the process of converting text into a vector of numbers. This is useful for similarity search. There are different techniques to embed the text like [HyDE](./techniques/embedding/hype-embedding.ipynb) and [HyPE](./techniques/embedding/hype-embedding.ipynb).

4. [Indexing](./techniques/indexing/README.md)
   Indexing is the process of loading, chunking, embedding and indexing of documents into a vector database. There are different techniques to index the documents like [Indexing API](./techniques/indexing/indexing-api.ipynb).

5. [Retriever](./techniques/retriever/README.md)
   Retriever is a component that retrieves relevant documents from a vector store. There are different types of retrievers like [Vector Store Retriever](./techniques/retriever/vector-store-retriever.ipynb), [BM25 Retriever](./techniques/retriever/bm25-retriever.ipynb), [Fusion Retriever or Hybrid Retriever](./techniques/retriever/fusion-retriever.ipynb) and [Reranker Retriever](./techniques/retriever/reranker-retriever.ipynb).

## RAG with LangGraph

> You can run these RAGs with [langgraph CLI](https://langchain-ai.github.io/langgraph/cloud/reference/cli/#langgraph-cli). Install the CLI with `pip install -U "langgraph-cli[inmem]"` and run `langgraph dev` to start the RAG.

1. [Naive RAG](./rag/naive_rag.py)
   Naive RAG is a simple RAG pipeline which has just 2 components:
   - Retriever Tool: A retriever that uses a vector store to retrieve relevant documents from a vector store.
   - Agent Node: A chat model that can answer user's question using the retriever tool.
