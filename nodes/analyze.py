from langchain_groq import ChatGroq

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

def analyze_node(state):
    prompt = f"""
Classify the question into ONE category:

- STATIC: general knowledge, explanations, concepts, definitions
- DYNAMIC: current events, latest data, real-time facts, changing info

Reply ONLY with STATIC or DYNAMIC.

Question: {state["question"]}
"""
    result = llm.invoke(prompt).content.strip().upper()

    return {
        "needs_search": result == "DYNAMIC"
    }
