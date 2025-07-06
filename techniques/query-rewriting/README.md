# Query Rewriting

Retrieval systems should ideally handle a wide range of queries from simple and poorly worded to complex and multi-faceted questions. To achieve this, we can use query rewriting techniques with the help of LLMs.

## Why it is useful?

- LLMs can rewrite ambiguous and poorly worded queries for clarity
- LLMs can generate more specific queries for better retrieval
- LLMs can breakdown complex queries into simpler ones

## What are the different types of query rewriting?

### [Multi-query](./multi-query-rewriting.ipynb)

Rewrite the query into multiple queries so that the retriever can retrieve the more unique and relevant documents. This technique is useful when you want to ensure high recall in retrieval by providing multiple phrasings of a question. This helps capture relevant documents that may match different ways of expressing the same information need.
