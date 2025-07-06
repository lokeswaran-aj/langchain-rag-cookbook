# Indexing

Indexing is the loading, chunking, embedding and indexing of documents into a vector database. One of the most issue with indexing is when we index the document second time, duplicate records are created in the vector database. So, resolve this issue langchain provides the [indexing API](https://python.langchain.com/docs/how_to/indexing/).

### How it works?

LangChain indexing uses a RecordManager to track document writes to the vector store.

For each document being indexed, the RecordManager stores:

- A document hash (computed from both content and metadata)
- The write timestamp
- A source ID (documents must include metadata identifying their source)

This allows LangChain to detect and handle duplicate documents during indexing.

### Deletion Modes

When indexing documents into a vector store, you may need to delete existing documents. The indexing API provides different deletion modes to handle this:

#### Mode Behaviors

- **None**: No automatic cleanup, we have to manually cleanup of old content
- **Incremental**:
  - Cleans up changed content continuously
  - Does not remove deleted source documents
  - Minimizes time when both old and new versions exist
- **Full**:
  - Cleans up changed content at end
  - Removes deleted source documents
  - Both versions may exist until final cleanup
- **Scoped_Full**:
  - Similar to Full but parallelizable
  - Does not remove deleted source documents
  - Both versions may exist until final cleanup

You can find the complete example in the [indexing-api.ipynb](./indexing-api.ipynb) notebook for PGVector.
