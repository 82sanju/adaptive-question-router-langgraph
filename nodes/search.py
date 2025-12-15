from langchain_groq import ChatGroq

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.2
)

def search_node(state):
    prompt = f"""
The user asked a time-sensitive question.
You do not have browsing access.

Clearly explain that the answer may change and provide
the most likely correct answer based on general knowledge.

Question: {state["question"]}
"""
    answer = llm.invoke(prompt).content

    return {"answer": answer}
