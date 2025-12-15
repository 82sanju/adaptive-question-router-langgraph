
# from langchain_groq import ChatGroq

# llm = ChatGroq(
#     model="llama-3.1-8b-instant",
#     temperature=0.3
# )

# def direct_answer_node(state):
#     answer = llm.invoke(state["question"]).content
#     return {"answer": answer}


from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.3
)

SYSTEM_PROMPT = """
You are a knowledgeable software engineering assistant.
You answer clearly and confidently.
If the question is about general concepts, frameworks,
or programming topics, explain them directly.
Do NOT say you lack information unless the topic is truly obscure.
"""

def direct_answer_node(state):
    messages = [
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(content=state["question"])
    ]

    response = llm.invoke(messages)

    return {
        "answer": response.content
    }
