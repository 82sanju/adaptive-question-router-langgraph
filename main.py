from graph import build_graph
from dotenv import load_dotenv
load_dotenv()

app = build_graph()

while True:
    question = input("\nAsk a question (or 'exit'): ")
    if question.lower() == "exit":
        break

    result = app.invoke({"question": question})
    print("\nAnswer:\n", result["answer"])
