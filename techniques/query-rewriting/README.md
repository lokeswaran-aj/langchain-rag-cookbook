# Query Rewriting

Retrieval systems should ideally handle a wide range of queries from simple and poorly worded to complex and multi-faceted questions. To achieve this, we can use query rewriting techniques with the help of LLMs.

## Why it is useful?

- LLMs can rewrite ambiguous and poorly worded queries for clarity
- LLMs can generate more specific queries for better retrieval
- LLMs can breakdown complex queries into simpler ones

## What are the different types of query rewriting?

### [Multi-query](./multi-query-rewriting.ipynb)

Rewrite the query into multiple queries so that the retriever can retrieve the more unique and relevant documents. This technique is useful when you want to ensure high recall in retrieval by providing multiple phrasings of a question. This helps capture relevant documents that may match different ways of expressing the same information need.

### [Decomposition](./decomposition-query-rewriting.ipynb)

When a question can be broken down into smaller subproblems. Decompose a question into a set of subproblems / questions, which can either be solved sequentially (use the answer from first + retrieval to answer the second) or in parallel (consolidate each answer into final answer).

### [Step-back](./step-back-query-rewriting.ipynb)

This technique is used to generate broader and more general queries that can help the retriever retrieve more relevant documents. This technique is used when a higher-level conceptual understanding is required.
