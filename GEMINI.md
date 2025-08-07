# Global Rules for AI-Driven Development

This file contains the universal, non-negotiable rules that govern ALL development work. These principles must be applied consistently in every task.

## 🧠 Core Architectural Philosophy: The "Analyst" Agent

The default architecture for any conversational agent is the **"Analyst" model**. This is a three-layer architecture designed for maximum flexibility and reliability.

1.  **Orchestrator (The Brain):** An LLM-driven component (`agent_orchestrator.py`) whose **sole purpose is to reason**. It analyzes conversational history and user intent to make two key decisions:
    a. **Tool Selection:** Which single tool is needed *right now*?
    b. **Parameter Extraction:** What information is needed to call that tool?
    c. **Synthesis:** After a tool returns raw data, the orchestrator's brain is used *again* to synthesize that data into a human-friendly response.

2.  **Tools (The Skills):** A collection of simple, deterministic Python functions (`tools/`). A tool's job is **to gather and prepare data**.
    -   A tool's primary responsibility is to interact with one or more services to fetch raw, unfiltered information.
    -   A tool SHOULD NOT contain complex decision-making logic (e.g., hardcoded rules for what is "good" or "bad" weather). This logic belongs in the Orchestrator's LLM brain.
    -   Tools MUST be stateless.

3.  **Services (The Senses):** The lowest-level clients (`services/`) that make direct API calls. Their job is **to connect to the outside world**.

## 🔄 The Core Development Workflow

1.  **Define Requirements (`product_requirement.md`)**: Define the "what" and the "why."
2.  **Generate a Plan (`generate-prp`)**: Create the master blueprint (the PRP).
3.  **Execute the Plan (`execute-prp`)**: Follow the PRP precisely.

## ✍️ Prompt Engineering Principles

-   **Context is King:** The System Prompt MUST be dynamically updated with the most recent conversational history to provide the LLM with the necessary context for multi-turn dialogue.
-   **Ask, Don't Assume ("Slot Filling"):** The agent's core logic must include asking the user for clarifying information if the parameters required for a tool are missing. The agent should never fail silently because of incomplete information.
-   **Explicit Instructions over Implicit Hope:** Prompts must be extremely explicit about the expected output format (e.g., "You MUST respond ONLY with a single, valid JSON object..."). They must also provide clear, step-by-step instructions on how the LLM should derive parameters from the conversation.

## ✅ Implementation & Validation Standards

-   **Stateful UI, Stateless Backend:** For interactive applications (like Streamlit), the UI layer (`app.py`) is responsible for managing the user session state (e.g., `st.session_state`, conversation UUIDs). The agent backend (`agent_orchestrator.py` and tools) MUST be designed to be stateless, simply receiving the current memory state for each call.
-   **Proactive Prerequisite Handling**: The process must stop and guide the user on how to set up the necessary environment.
-   **Test-Driven Implementation**: Every tool MUST have a corresponding unit test.
-   **Comprehensive Error Handling**: All functions involving network requests or parsing external data MUST be wrapped in `try...except` blocks.

## 🚫 Anti-Patterns to ALWAYS AVOID

-   ❌ **NEVER** embed complex, rigid decision-making logic into a Tool. Let the LLM reason over raw data.
-   ❌ **NEVER** create a "monolithic" tool that tries to do many different things. Decompose into small, single-purpose tools.
-   ❌ **NEVER** hardcode secrets. Use a configuration system.
-   ❌ **NEVER** take an action (e.g., create a calendar event) without explicit user confirmation.