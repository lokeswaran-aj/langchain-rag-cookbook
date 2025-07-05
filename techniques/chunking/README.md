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

The most simplest technique to split the document into chunks by a certain **fixed length**. This is naive but keeps the chunks consistent. But the texts are split in the middle of a word if the word is longer than the chunk size. We can use the `CharacterTextSplitter` class from `langchain_text_splitter` to split the document into chunks.

### Text-based chunking

This is similar to Length-based chunking but instead of splitting by a certain number of characters, it splits by a certain number of words. This is more accurate than Length-based chunking. But the chunks are not split in a meaningful way. We can use the `RecursiveCharacterTextSplitter` class from `langchain_text_splitter` to split the document into chunks.

### Semantic-based chunking

This is a more advanced technique that splits the document into chunks based on the semantic meaning of the text. This is more accurate than Length-based chunking and Text-based chunking. This chunker works by determining when to "break" apart sentences. This is done by looking for differences in embeddings between any two sentences. When that difference is past some threshold, then they are split.
There are a few ways to determine what that threshold is, which are controlled by the `breakpoint_threshold_type` kwarg.

- `percentile`: In this method, all differences between sentences are calculated, and then any difference greater than the X percentile is split. The default value for X is 95.0
- `interquartile`: In this method, the interquartile distance is used to split chunks. The default value is 1.5.
- `standard_deviation`: In this method, any difference greater than X standard deviations is split. The default is 3.0.
- `gradient`: In this method, the gradient of distance is used to split chunks along with the percentile method. This method is useful when chunks are highly correlated with each other or specific to a domain. The default value is 95.0.

We can use the `SemanticChunker` class from `langchain_experimental.text_splitter` to split the document into chunks.

### Document-based chunking

This is a more advanced technique that splits the document into chunks based on the file type and the syntax of the document. This is useful when the document is a codebase. We can use the `MarkdownTextSplitter` class from `langchain_text_splitter` to split the markdown document into chunks.

We can also use the `PythonCodeTextSplitter` class from `langchain_text_splitter` to split the python code into chunks.

We can also use the `RecursiveCharacterTextSplitter.from_language` with the `Language` enum from `langchain_text_splitter` to split the javascript code into chunks based on the language of the document.
