import os

from langchain.indexes import SQLRecordManager, index
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import PGVector
from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai import OpenAIEmbeddings
from rich import print

# Get the current directory path
current_dir = os.path.dirname(os.path.abspath(__file__))
pdf_path = os.path.join(current_dir, "aiaun.pdf")

documents = PyPDFLoader(pdf_path).load()
print("documents", len(documents), documents[0])
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
text_splitter = SemanticChunker(
    embeddings=embeddings, breakpoint_threshold_type="interquartile"
)

chunks = text_splitter.split_documents(documents)
print("chunks", len(chunks), chunks[0])
COLLECTION_NAME = "my_collection"
DATABASE_URL = os.getenv("DATABASE_URL")

vector_store = PGVector.from_documents(
    documents=[],
    embedding=embeddings,
    connection_string=DATABASE_URL,
    collection_name=COLLECTION_NAME,
    create_extension=True,
    use_jsonb=True,
)

namespace = f"pgvector/{COLLECTION_NAME}"
record_manager = SQLRecordManager(namespace=namespace, db_url=DATABASE_URL)
record_manager.create_schema()

result = index(
    docs_source=chunks,
    record_manager=record_manager,
    vector_store=vector_store,
    cleanup="incremental",
    source_id_key="source",
)
print(result)
