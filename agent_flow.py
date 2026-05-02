from langgraph.graph import StateGraph, END
from schema import AgentState
from vector_engine import retrieve
from search_tool import web_search
from llm_client import generate_answer


# ---------------- ROUTER ----------------
def router(state):
    q = state["query"].lower()

    if "debales" in q:
        return {**state, "mode": "rag"}
    return {**state, "mode": "serp"}


# ---------------- RAG NODE ----------------
def rag_node(state, db):
    context = retrieve(db, state["query"])
    return {**state, "context": context}


# ---------------- SERP NODE ----------------
def serp_node(state):
    context = web_search(state["query"])
    return {**state, "context": context}


# ---------------- GENERATOR ----------------
def final_answer(state):
    prompt = f"""
Use context to answer clearly:

Context:
{state['context']}

Question:
{state['query']}
"""

    ans = generate_answer(prompt)
    return {**state, "response": ans}


def decide(state):
    return state["mode"]


# ---------------- BUILD GRAPH ----------------
def build_agent(db):
    graph = StateGraph(AgentState)

    graph.add_node("router", router)
    graph.add_node("rag", lambda s: rag_node(s, db))
    graph.add_node("serp", serp_node)
    graph.add_node("generate", final_answer)

    graph.set_entry_point("router")

    graph.add_conditional_edges(
        "router",
        decide,
        {
            "rag": "rag",
            "serp": "serp"
        }
    )

    graph.add_edge("rag", "generate")
    graph.add_edge("serp", "generate")
    graph.add_edge("generate", END)

    return graph.compile()