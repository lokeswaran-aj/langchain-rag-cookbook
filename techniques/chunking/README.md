# Chunking

Chunking is a technique that involves breaking down a large document into smaller, more manageable chunks for efficient processing and analysis. A document in this context can refer to various types of content, including:

- Text from a single file
- Content from multiple files in a folder
- Web pages or entire websites
- Code repositories
- Databases or structured data

The goal of chunking is to preserve the semantic meaning and context while creating smaller units that can be processed independently.

## Why is it useful?

- To overcome the context window limit of LLMs
- To ensure consistent processing of documents with different lengths
- To improve the retrieval of relevant information from the document
- To optimize the cost of processing the document

## What are the different types of chunking?

### Length-based chunking

The most simplest technique to split the document into chunks by a certain **fixed length**. This is naive but keeps the chunks consistent. But the texts are split in the middle of a word if the word is longer than the chunk size.
