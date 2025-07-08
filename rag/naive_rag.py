import os

from langchain_community.vectorstores import PGVector
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langgraph.graph import START, MessagesState, StateGraph
from langgraph.prebuilt import ToolNode, tools_condition

# Setup vector store
embeddings = OpenAIEmbeddings()
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


# Setup Retriever Tool
@tool
def retriever(query: str) -> list[str]:
    """Retrieve relevant documents related to Vercel's AI SDK from the vector store based on the query."""
    vector_retriever = vector_store.as_retriever(search_kwargs={"k": 5})
    docs = vector_retriever.invoke(query)
    return docs


# Setup LLM
llm = ChatOpenAI(model="gpt-4o-mini").bind_tools([retriever])


# Setup an agent node
def agent(state: MessagesState):
    response = llm.invoke(state["messages"])
    return {"messages": [response]}


# Setup a tool node
tool_node = ToolNode(tools=[retriever])

# Setup a graph
graph = StateGraph(MessagesState)

graph.add_node("agent", agent)
graph.add_node("tools", tool_node)

graph.add_conditional_edges("agent", tools_condition)
graph.add_edge("tools", "agent")
graph.add_edge(START, "agent")

graph.compile()
