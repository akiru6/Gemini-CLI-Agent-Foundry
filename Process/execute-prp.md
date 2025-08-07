# Execute Product Requirement Prompt (PRP)

## Goal
To reliably implement a complex, multi-tool, conversational software project from a PRP, following an incremental and test-driven methodology.


## Inputs
- **`--prp`**: The **required path** to the PRP file that contains the complete project specification, including the implementation plan and validation loop.
   - *`PRPs/*.prp.md`*
   
## Execution Process

### Phase 1: PRP Comprehension and Prerequisite Validation
1.  **Load and Ingest PRP:** Read all sections of the PRP. It is the single source of truth.
2.  **Prerequisite Check:** Immediately find and execute the `Prerequisites & Setup Guide`. If any environment variables are missing, **STOP** and report to the user with the guide.

### Phase 2: Incremental, Test-Driven Implementation

**Follow this strict bottom-up order to build the application:**

1.  **Implement the Services Layer First (`services/`):**
    -   Write the code for all the low-level API clients.
    -   *There are typically no unit tests for these simple clients.*
2.  **Implement the Tools Layer Next (`tools/`):**
    -   Write the code for each individual tool.
    -   **After implementing EACH tool, immediately write its corresponding unit test.**
    -   Run the unit tests for the tools and ensure they pass before proceeding. This validates the data-gathering layer is working correctly.
3.  **Implement the Orchestrator (`agent_orchestrator.py`):**
    -   Write the code for the main agent brain, including the logic for calling the LLM and the tools.
4.  **Implement the UI Layer Last (`app.py`):**
    -   Write the code for the Streamlit application and wire it to the orchestrator.

### Phase 3: Full-System Validation
1.  **Static Analysis:** Run `ruff`, `mypy` on the entire codebase.
2.  **Unit Tests:** Run the full `pytest` suite again to ensure no regressions.
3.  **Manual End-to-End Test:** Run the Streamlit application and manually test the conversational flows as described in the PRP's validation loop.

### Phase 4: Final Review
1.  Consult the PRP's checklist and report completion status.