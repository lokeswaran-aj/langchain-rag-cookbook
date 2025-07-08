import os

from langchain.indexes import SQLRecordManager, index
from langchain_community.document_loaders.sitemap import SitemapLoader
from langchain_community.vectorstores import PGVector
from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai import OpenAIEmbeddings
from rich import print

loader = SitemapLoader(
    web_path="https://ai-sdk.dev/sitemap.xml",
    filter_urls=["https://ai-sdk.dev/docs/foundations"],
)

docs = loader.load()

print(f"There are {len(docs)} documents loaded")


embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

text_splitter = SemanticChunker(
    embeddings=embeddings,
    add_start_index=True,
    breakpoint_threshold_type="gradient",
    breakpoint_threshold_amount=75,
    min_chunk_size=500,
)
chunks = text_splitter.split_documents(docs)

for c in chunks:
    print(len(c.page_content))

COLLECTION_NAME = "ai-sdk-docs"
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
    key_encoder="sha512",
)
print(result)
