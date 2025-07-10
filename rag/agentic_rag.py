import os
from typing import Literal

from langchain.tools import tool
from langchain_community.vectorstores import PGVector
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langgraph.graph import END, START, MessagesState, StateGraph
from langgraph.prebuilt import ToolNode, tools_condition
from pydantic import BaseModel, Field

embeddings = OpenAIEmbeddings()
COLLECTION_NAME = "ai-sdk-docs"
DATABASE_URL = os.getenv("DATABASE_URL")

vector_store = PGVector(
    collection_name=COLLECTION_NAME,
    connection_string=DATABASE_URL,
    use_jsonb=True,
    embedding_function=embeddings,
)

GENERATE_ANSWER_PROMPT = (
    "You are an assistant for question-answering tasks. "
    "Use the following pieces of retrieved context to answer the question. "
    "If you don't know the answer, just say that you don't know. \n"
    "Question: {question} \n"
    "Context: {context}"
)

GRADE_PROMPT = (
    "You are a grader assessing relevance of a retrieved document to a user question. \n "
    "Here is the retrieved document: \n\n {context} \n\n"
    "Here is the user question: {question} \n"
    "If the document contains keyword(s) or semantic meaning related to the user question, grade it as relevant. \n"
    "Give a binary score 'yes' or 'no' score to indicate whether the document is relevant to the question."
)

REWRITE_QUESTION_PROMPT = (
    "Look at the input and try to reason about the underlying semantic intent / meaning.\n"
    "Here is the initial question:"
    "\n ------- \n"
    "{question}"
    "\n ------- \n"
    "Formulate an improved question:"
)


# Setup Retriever Tool
@tool
def retriever(query: str) -> list[str]:
    """Retrieve relevant documents related to Vercel's AI SDK from the vector store based on the query."""
    vector_retriever = vector_store.as_retriever(search_kwargs={"k": 5})
    docs = vector_retriever.invoke(query)
    return docs


llm = ChatOpenAI(model="gpt-4o-mini")


def generate_retrieval_query_or_respond(state: MessagesState):
    llm_with_retriever = llm.bind_tools([retriever])
    response = llm_with_retriever.invoke(state["messages"])
    return {"messages": [response]}


class Grade(BaseModel):
    binary_score: str = Field(
        description="Relevance score: 'yes' if relevant, or 'no' if not relevant"
    )


def grade_documents(
    state: MessagesState,
) -> Literal["generate_answer", "rewrite_question"]:
    question = state["messages"][0].content
    retrieved_documents = state["messages"][-1].content

    prompt = GRADE_PROMPT.format(context=retrieved_documents, question=question)
    grade_llm = llm.with_structured_output(Grade)
    response = grade_llm.invoke([HumanMessage(content=prompt)])
    grade = response.binary_score

    if grade == "yes":
        return "generate_answer"
    else:
        return "rewrite_question"


def generate_answer(state: MessagesState):
    question = state["messages"][0].content
    retrieved_documents = state["messages"][-1].content
    prompt = GENERATE_ANSWER_PROMPT.format(
        question=question, context=retrieved_documents
    )
    response = llm.invoke([HumanMessage(content=prompt)])
    return {"messages": [response]}


def rewrite_question(state: MessagesState):
    question = state["messages"][0].content
    prompt = REWRITE_QUESTION_PROMPT.format(question=question)
    response = llm.invoke([HumanMessage(content=prompt)])
    return {"messages": [HumanMessage(content=response.content)]}


builder = StateGraph(MessagesState)

builder.add_node(
    "generate_retrieval_query_or_respond", generate_retrieval_query_or_respond
)
builder.add_node("generate_answer", generate_answer)
builder.add_node("rewrite_question", rewrite_question)
builder.add_node("retriever", ToolNode(tools=[retriever]))

builder.add_edge(START, "generate_retrieval_query_or_respond")
builder.add_conditional_edges(
    "generate_retrieval_query_or_respond",
    tools_condition,
    {"tools": "retriever", END: END},
)
builder.add_conditional_edges("retriever", grade_documents)
builder.add_edge("rewrite_question", "generate_retrieval_query_or_respond")
builder.add_edge("generate_answer", END)

graph = builder.compile()
