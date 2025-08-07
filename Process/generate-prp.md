# Generate Product Requirement Prompt (PRP)

## Goal
To create a comprehensive PRP for a **multi-tool, conversational AI agent**, ensuring a high probability of successful implementation.

## Inputs
- `--requirement`: Path to the PRD file.
  - *`PRPs/product_requirement.md`*
- `--template`: Glob pattern for Technical Blueprints.
  - *`PRPs/templates/*.md`*
- `--output`: Path for the final PRP file.
  - *`PRPs/*{prp_name}*.prp.md`*

## Execution Process

### Phase 1: Research & Context Gathering (Architectural Discovery)

<!-- 
    IMPROVEMENT: This phase is now highly specific, instructing the agent on exactly
    what sources to consult and how to consult them. This makes the research process
    concrete and repeatable.
-->

1.  **Understand the Core Goal from the PRD:**
    -   Read and fully comprehend the file at the `--requirement` path 
        - *`PRPs/product_requirement.md`*
    -   Identify the key business goals, desired features, and all mentioned technologies (e.g., "Google Calendar", "Open-Meteo").

2.  **Conduct Multi-Source Research (Internal & External):**

    a. **Scan Available Blueprints:**
       -   Using the `--template` glob pattern, find and analyze all available blueprint files.
            - *`PRPs/templates/*.md`*
       -   Identify high-level architectural ideas, validation patterns, and task structures. Do not select one yet; gather all ideas.

    b. **Investigate Concrete Examples:**
       -   **Action:** List the contents of the `examples/` directory to understand what proven, working code is available.
       -   **Action:** Based on the PRD's goal, identify the most relevant example project(s) within the `examples/` folder.
       -   **Action:** Read the source code of the most relevant example(s). Pay close attention to how they structure their `main` functions, handle configuration, and define their tools. Concrete examples often provide more robust patterns than abstract blueprints.

    c. **Find External Best Practices & Official Docs:**
       -   **Action:** Use the `search` tool to find the most current **official documentation** for the key technologies identified in the PRD.
       -   *Example Searches:* "Google Calendar API Python client quickstart", "Open-Meteo API docs", "google-auth-oauthlib refresh token flow".
       -   Focus on API contracts (required parameters, response structures), authentication mechanisms (especially OAuth 2.0 flows), and recommended usage patterns. This step is critical for avoiding bugs and using the latest, most secure methods.

### Phase 2: Synthesis & Planning (ULTRATHINK)

1.  **Architect the Solution:**
    -   Critically evaluate all gathered information from Phase 1.
    -   **Synthesize the best patterns.** For example: use the file structure from a blueprint, the dependency management from an `example`, and the precise API call format from the official external documentation.
    -   If there is a conflict between sources, **the official external documentation is the highest authority**, followed by concrete examples, then abstract blueprints.

2.  **Formulate a Detailed Plan:**
    -   Create a clear, step-by-step plan for the final PRP, outlining which specific patterns you will use and justifying *why* based on your research.

### Phase 3: PRP Construction (Building the Enhanced Blueprint)

1.  **Goal & Context Sections:** Write a clear "Goal" and a comprehensive "All Needed Context" section. In the context, **explicitly cite your sources**, including links to the external documentation you found and file paths to the specific examples you referenced. This makes your architectural decisions traceable.

2.  **Prerequisites & Setup Section:**
    -   Create a dedicated section `## Prerequisites & Setup Guide`.
    -   List all required environment variables.
    -   Provide a high-level guide on how to obtain complex credentials, referencing the official documentation you found in your research.

3.  **Implementation Blueprint & Validation Loop Sections:**
    -   Define Pydantic models, tasks, and pseudocode based on your architected solution.
    -   Construct a multi-level `Validation Loop` starting with a "Level 0: Pre-flight Check".

### Phase 4: Finalization & Output

1.  **Combine and Refine:** Assemble all sections into a single markdown file.
2.  **Save Output:** Save the final PRP to the `--output` path.
3.  **Perform Quality Check** and assign a confidence score.

## Final Review & Quality Score
- [ ] **Completeness**: Is all necessary context from the PRD, codebase research, and external best practices included?
- [ ] **Clarity & Actionability**: Is the `Prerequisites & Setup Guide` clear and based on official documentation?
- [ ] **Traceability**: Does the PRP cite its sources, explaining *why* certain architectural patterns were chosen? <!-- NEW, IMPORTANT CHECK -->
- [ ] **Executability**: Is the `Validation Loop` structured logically and reliably?
- [ ] **Robustness**: Are potential errors, edge cases, and security considerations documented?

**Confidence Score (1-10):** Assign a score.