from langgraph.graph import StateGraph, END
from state import AgentState
from dotenv import load_dotenv
load_dotenv()


from nodes.analyze import analyze_node
from nodes.direct_answer import direct_answer_node
from nodes.search import search_node

def route_decision(state):
    print("Routing decision — needs_search:", state["needs_search"])
    return "search" if state["needs_search"] else "direct_answer"


def build_graph():
    graph = StateGraph(AgentState)

    graph.add_node("analyze", analyze_node)
    graph.add_node("direct_answer", direct_answer_node)
    graph.add_node("search", search_node)

    graph.set_entry_point("analyze")

    graph.add_conditional_edges(
        "analyze",
        route_decision,
        {
            "direct_answer": "direct_answer",
            "search": "search"
        }
    )

    graph.add_edge("direct_answer", END)
    graph.add_edge("search", END)

    return graph.compile()
