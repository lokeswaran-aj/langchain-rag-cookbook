# rag-cookbook-langchain

This is a collection of notebooks that I used to learn about RAG with LangChain.

There are separate notebooks for each technique.

## Techniques

1. [Chunking](./techniques/chunking/README.md)
   Chunking is the process of splitting the document into smaller chunks so that it can be processed by the LLM. There are different techniques to chunk the document like [length-based](./techniques/chunking/length-based-chunking.ipynb), [text-based](./techniques/chunking/text-based-chunking.ipynb), [semantic-based](./techniques/chunking/semantic-based-chunking.ipynb), and [document-based](./techniques/chunking/document-based-chunking.ipynb).

2. [Query Rewriting](./techniques/query-rewriting/README.md)
   Query rewriting is the process of rewriting the query to make it more specific and relevant to the document. There are different techniques to rewrite the query like [multi-query](./techniques/query-rewriting/multi-query-rewriting.ipynb), [decomposition](./techniques/query-rewriting/decomposition-query-rewriting.ipynb) and [step-back](./techniques/query-rewriting/step-back-query-rewriting.ipynb)

3. [Embedding](./techniques/embedding/README.md)
   Embedding is the process of converting text into a vector of numbers. This is useful for similarity search. There are different techniques to embed the text like [HyDE](./techniques/embedding/hype-embedding.ipynb) and [HyPE](./techniques/embedding/hype-embedding.ipynb).
