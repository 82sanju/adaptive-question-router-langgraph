
---

Adaptive Question Router Agent
LangGraph Module 4

---

## OVERVIEW

This project implements an adaptive AI agent using LangGraph Module 4 that intelligently routes user questions based on their intent and time-sensitivity.

Instead of relying on linear prompt chaining, the agent uses a state-driven graph with conditional execution to decide whether a question should be answered directly using an LLM’s general knowledge or handled via a search-aware fallback path.

The system is powered by Groq’s LLaMA-3 models and follows production-style agent design patterns.

---

## HOW IT WORKS

1. The user enters a question.
2. The analyze (router) node classifies the question as:

   * STATIC: general knowledge or conceptual questions
   * DYNAMIC: time-sensitive or real-world changing information
3. Based on this classification, the graph routes execution to:

   * A direct answer node for STATIC questions
   * A search-aware node for DYNAMIC questions
4. The agent returns a controlled and deterministic response.

All decisions are driven by explicit state rather than prompt-based heuristics.

---

## KEY FEATURES

* Conditional routing using LangGraph Module 4
* State-based execution flow
* Groq LLaMA-3.3-70B model for routing decisions
* Groq LLaMA-3.1-8B model for fast responses
* Clear separation of responsibilities between nodes
* Extensible design for retries, human-in-the-loop workflows, and persistence

---

## ARCHITECTURE

User Question
|
Analyze Node (Router)
|
-

|                   |
Direct Answer     Search-Aware Answer
|                   |
-------- END --------

---

## TECH STACK

* Python
* LangGraph
* LangChain
* Groq API (LLaMA-3)
* python-dotenv

---

## SETUP AND RUN

1. Clone the repository
   git clone [https://github.com/](https://github.com/82sanju/adaptive-question-router-langgraph.git)
   cd adaptive-question-router-langgraph

2. Create and activate a virtual environment
   python -m venv venv
   venv\Scripts\Activate  (Windows)
   source venv/bin/activate  (macOS/Linux)

3. Install dependencies
   pip install -r requirements.txt

4. Create a .env file in the project root
   GROQ_API_KEY=your_groq_api_key_here

5. Run the application
   python main.py

---

## WHY THIS PROJECT MATTERS

Most LLM demos rely on simple prompt chaining.

This project demonstrates real-world agent engineering concepts:

* Execution control instead of prompt chaos
* Graph-based reasoning
* Deterministic and debuggable workflows
* A scalable foundation for production AI systems

---

## FUTURE IMPROVEMENTS

* Retry and evaluation loops
* Human-in-the-loop approval (LangGraph Module 5)
* Persistent state and checkpoints
* Real-time search integration (Tavily or SerpAPI)
* Multi-agent or supervisor graph architecture

---

## LICENSE

MIT License

---
