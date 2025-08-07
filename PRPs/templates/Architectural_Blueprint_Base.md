# Technical Blueprint: The Conversational Analyst Agent

A technical specification for a multi-skill, conversational AI agent with a web interface, session memory, and an "Analyst" reasoning core.

## 1. Core Architecture: The "Analyst" Model

This agent MUST be built using the three-layer "Analyst" architecture.

1.  **Orchestrator (The Brain):** An LLM-driven module (`agent_orchestrator.py`). Its primary role is to **reason**. It analyzes conversation history to select tools and, most importantly, to **synthesize raw data from tools into intelligent, human-friendly responses and plans.**
2.  **Tools (The Skills):** Simple, deterministic Python functions (`tools/`). A tool's job is **only to gather and prepare data**. Tools MUST NOT contain complex decision-making logic (e.g., filtering).
3.  **Services (The Senses):** Low-level clients (`services/`) that make direct API calls.

## 2. Prerequisites & Setup Guide

To run this agent, you must configure your environment. Create a file named `.env` in the project root and populate it with the following keys. Here is how to obtain each required value:

### 1. LLM API Key (Google Gemini)
-   **`GEMINI_API_KEY`**: Obtain this from the [Google AI Studio](https://ai.google.dev/) website. Create a new API key in your project.

### 2. Google API Credentials (for Calendar)

This is a multi-step process involving the Google Cloud Console.

#### Part A: Project and Client Credentials
-   **`GCP_PROJECT_ID`**: Your Google Cloud Project ID.
-   **`GCP_CLIENT_ID`**: The OAuth 2.0 Client ID.
-   **`GCP_CLIENT_SECRET`**: The OAuth 2.0 Client Secret.

**How to get them:**
1.  Go to the [Google Cloud Console](https://console.cloud.google.com/).
2.  Create a new project (or select an existing one). Your **Project ID** is visible on the dashboard.
3.  In the navigation menu, go to "APIs & Services" > "Enabled APIs & services" and enable the **"Google Calendar API"**.
4.  Go to "APIs & Services" > "Credentials". Click "+ CREATE CREDENTIALS" and select "OAuth client ID".
5.  Choose **"Desktop app"** as the application type.
6.  After creation, a window will pop up with your **Client ID** and **Client Secret**. Copy these values. You can also download the `credentials.json` file for use in the next step.

#### Part B: User Refresh Token (CRITICAL)
-   **`USER_REFRESH_TOKEN`**: This is a special token that allows the agent to access your calendar on your behalf without you having to log in every time.

**How to get it:**
The most reliable way is to use a helper script (`generate_token.py` is a common name for it) that runs a one-time authentication flow.
1.  Download the `credentials.json` file from the OAuth client ID page in the Google Cloud Console and place it in your project root.
2.  Run the helper script (e.g., `python generate_token.py`).
3.  The script will open a browser window. Log in with the Google account whose calendar you want the agent to manage.
4.  Approve the permissions request.
5.  The script will then print a **Refresh Token** to your terminal. Copy this long string of characters.

---
**Final `.env.example` structure:**
```
# .env.example - Copy this to .env and fill in your values

# Google Gemini API Key
GEMINI_API_KEY="your_gemini_api_key_here"

# Google Cloud Project Credentials
GCP_PROJECT_ID="your-gcp-project-id-here"
GCP_CLIENT_ID="your-gcp-client-id.apps.googleusercontent.com"
GCP_CLIENT_SECRET="your-gcp-client-secret-here"

# Google User Refresh Token
USER_REFRESH_TOKEN="your_long_user_refresh_token_here"
```

## 3. Agent Capabilities & Tool Design

The agent's intelligence is in its brain, not its tools. The toolset should be simple and focused on data gathering.

1.  **`get_weather_data_tool` (Primary Tool):**
    -   **Purpose**: To fetch raw, unfiltered hourly weather data.
    -   **Parameters**: `city: str`, `time_range: str` (a flexible, natural language string like "tonight" or "this weekend").
    -   **Returns**: A list of raw `HourlyForecast` data points.

2.  **`google_calendar_tool`:**
    -   **Purpose**: To execute the creation of a calendar event.
    -   **Parameters**: `summary: str`, `start_time: str`, `end_time: str`, `timezone: str`.
    -   **Returns**: A confirmation string with the new event's ID.

**NOTE:** Do NOT create a separate "planning" tool. The act of "planning" is a reasoning task for the Orchestrator, which it will perform after gathering data with the `get_weather_data_tool`.

## 4. Agent Behavior & Reasoning (System Prompt Guidance)

The Orchestrator's System Prompt is the most critical component. It MUST instruct the LLM to:
1.  **Analyze Intent:** Determine if the user wants a weather report, wants to plan an activity, or is confirming an action.
2.  **Ask for Missing Info ("Slot Filling"):** If a tool's required parameters (like `city`) are not in the conversation, the LLM's job is to ask a clarifying question.
3.  **Follow the "Gather-Then-Synthesize" Loop:**
    -   **For planning:** The LLM's first action is to call `get_weather_data_tool` to gather data. Then, in a subsequent turn, it will receive that data and be prompted to act as an "expert planner," analyzing the data to form a recommendation.
    -   **For weather reports:** The LLM first calls `get_weather_data_tool`. Then, it is prompted to act as a "weather reporter," summarizing the raw data into a paragraph.
4.  **Extract All Parameters from History:** For actions like `google_calendar_tool`, the prompt must instruct the LLM to scan the entire recent history to find all the required parameters (summary, time, timezone).

## 5. Desired Codebase Tree

```bash
.
├── .env.example
├── memory_conversations/       # Directory for session files
├── pyproject.toml
├── app.py                      # Streamlit UI
└── src/
    ├── __init__.py
    ├── config.py
    ├── models.py
    ├── agent_orchestrator.py   # The "Analyst" Brain
    ├── memory_manager.py       # Manages conversation files
    ├── tools/
    │   ├── __init__.py
    │   └── weather_report_tool.py # The primary data tool
    │   └── calendar_tool.py
    └── services/
        ├── __init__.py
        ├── geocoding_client.py
        ├── open_meteo_client.py
        └── google_calendar.py
```

## 6. Implementation Blueprint (Task Order)

The project MUST be built in this bottom-up order:
1.  **Setup & Scaffolding**: Create files, setup `.env`.
2.  **Services & Models**: Implement all low-level clients and Pydantic models.
3.  **Tools**: Implement and unit-test the data-gathering tools.
4.  **Memory Manager**: Implement the session file handler.
5.  **Orchestrator**: Implement the core reasoning and synthesis logic.
6.  **UI**: Implement the Streamlit app and connect it to the Orchestrator.

## 7. Validation Loop

This is the multi-level process to ensure the application is fully functional and correct.

### Level 0: Pre-flight Check (Automated)
This check MUST run first. It verifies that the environment is set up correctly.
```bash
# A simple script or command to check for the existence of the .env file
python -c "import os; assert os.path.exists('.env'), '.env file not found. Please copy .env.example to .env and fill in your credentials.'" && echo "✅ .env file found."
```

### Level 1: Static Analysis & Formatting (Automated)
These commands ensure code quality and consistency.
```bash
uv run ruff format .
uv run ruff check . --fix
uv run mypy src/
```
**Expected Outcome:** No errors from any command.

### Level 2: Unit Tests (Automated)
This validates the internal logic of our tools without needing any API keys or network connection.
```bash
uv run pytest tests/
```
**Expected Outcome:** All unit tests pass, confirming the data-gathering tools work as expected with mock data.

### Level 3: Manual End-to-End Test (Human-in-the-loop)
This is the final acceptance test to validate the complete conversational intelligence of the agent.

**Command to start the application:**
```bash
streamlit run app.py
```

**Test Scenarios Checklist:**

-   [ ] **Scenario 1: Slot Filling**
    -   **User:** "I want to have a city walk tonight."
    -   **Expected Kai:** Asks a clarifying question like, "That sounds lovely! Which city are you in?"
    -   **User:** "Shanghai"
    -   **Expected Kai:** Proceeds to gather weather data for Shanghai and gives a proposal.

-   [ ] **Scenario 2: Direct Weather Report**
    -   **User:** "What's the weather like in London tomorrow?"
    -   **Expected Kai:** Provides a detailed, human-readable paragraph summarizing the weather for the full day in London.

-   [ ] **Scenario 3: Full Planning Flow & Confirmation**
    -   **User:** "Find a good time for a 2-hour bike ride in Paris this weekend."
    -   **Expected Kai:** Gathers weather for the upcoming weekend in Paris, analyzes it, and proposes the best-looking multi-hour window (e.g., "The best time for your bike ride looks to be Saturday afternoon from 2 PM to 5 PM, when it will be sunny and around 22°C. How does that sound?").
    -   **User:** "Yes, that sounds perfect. Please schedule it."
    -   **Expected Kai:** Creates the event on Google Calendar and responds with a confirmation message like, "Done! I've added it to your calendar."

-   [ ] **Scenario 4: Session Management**
    -   Complete Scenario 3.
    -   Click the "➕ New Conversation" button in the sidebar.
    -   **Expected:** The chat history clears.
    -   **User:** "How's the weather here?"
    -   **Expected Kai:** Asks for the city again, demonstrating that the context from the previous conversation has been correctly isolated.

