# PRP: Kai - The Conversational Weather Advisor

## 1. Goal

To build "Kai," a conversational AI agent that acts as a personal weather advisor. Kai will be able to provide weather forecasts, analyze weather conditions to recommend activities, and schedule events on the user's Google Calendar. The agent will be accessible through a web-based chat interface and will maintain conversational context.

## 2. All Needed Context

This plan is based on a synthesis of the following sources:

*   **Internal Product Requirement:** `PRPs/product_requirement.md`
*   **Internal Architectural Blueprint:** `PRPs/templates/Architectural_Blueprint_Base.md`
*   **Internal Code Examples:** `examples/streamlit_app.py` and `examples/agent_with_memory.py`
*   **External Documentation:**
    *   **Open-Meteo API:** [https://open-meteo.com/en/docs](https://open-meteo.com/en/docs)
    *   **Google Calendar API Python Quickstart:** [https://developers.google.com/calendar/api/guides/python](https://developers.google.com/calendar/api/guides/python)

## 3. Prerequisites & Setup Guide

### 1. Environment Variables

Create a `.env` file in the project root with the following content:

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

### 2. Obtaining Credentials

*   **`GEMINI_API_KEY`**: Obtain this from [Google AI Studio](https://ai.google.dev/).
*   **Google Calendar API Credentials (`GCP_PROJECT_ID`, `GCP_CLIENT_ID`, `GCP_CLIENT_SECRET`, `USER_REFRESH_TOKEN`):** Follow the instructions in the `Architectural_Blueprint_Base.md` to create a Google Cloud project, enable the Google Calendar API, and generate an OAuth 2.0 client ID and refresh token. A helper script named `generate_token.py` will be required to obtain the `USER_REFRESH_TOKEN`.

## 4. Implementation Blueprint

### 1. Codebase Structure

```bash
.
├── .env.example
├── memory_conversations/
├── pyproject.toml
├── app.py
└── src/
    ├── __init__.py
    ├── config.py
    ├── models.py
    ├── agent_orchestrator.py
    ├── memory_manager.py
    ├── tools/
    │   ├── __init__.py
    │   ├── weather_report_tool.py
    │   └── calendar_tool.py
    └── services/
        ├── __init__.py
        ├── open_meteo_client.py
        └── google_calendar.py
```

### 2. Models

**`src/models.py`**

```python
from pydantic import BaseModel
from typing import List

class HourlyForecast(BaseModel):
    time: str
    temperature_2m: float
    relativehumidity_2m: int
    precipitation_probability: int
    windspeed_10m: float

class WeatherData(BaseModel):
    hourly: List[HourlyForecast]

class CalendarEvent(BaseModel):
    summary: str
    start_time: str
    end_time: str
    timezone: str
```

### 3. Services

*   **`src/services/open_meteo_client.py`**: A client to interact with the Open-Meteo API.
*   **`src/services/google_calendar.py`**: A client to interact with the Google Calendar API.

### 4. Tools

*   **`src/tools/weather_report_tool.py`**:
    *   `get_weather_data_tool(city: str, time_range: str)`: Fetches raw weather data from the Open-Meteo service.
*   **`src/tools/calendar_tool.py`**:
    *   `create_calendar_event_tool(summary: str, start_time: str, end_time: str, timezone: str)`: Creates an event in Google Calendar.

### 5. Orchestrator

*   **`src/agent_orchestrator.py`**: The "Analyst" brain. It will use the tools to gather data and then synthesize it into helpful responses and plans.

### 6. UI

*   **`app.py`**: A Streamlit application based on `examples/streamlit_app.py`.

## 5. Validation Loop

### Level 0: Pre-flight Check

```bash
python -c "import os; assert os.path.exists('.env'), '.env file not found. Please copy .env.example to .env and fill in your credentials.'" && echo "✅ .env file found."
```

### Level 1: Static Analysis & Formatting

```bash
uv run ruff format .
uv run ruff check . --fix
uv run mypy src/
```

### Level 2: Unit Tests

```bash
uv run pytest tests/
```

### Level 3: Manual End-to-End Test

**Command to start the application:**

```bash
streamlit run app.py
```

**Test Scenarios:**

*   [ ] **Scenario 1: Slot Filling**
    *   **User:** "I want to have a city walk tonight."
    *   **Expected Kai:** Asks for the city.
    *   **User:** "Shanghai"
    *   **Expected Kai:** Provides a weather-based proposal for a walk in Shanghai.
*   [ ] **Scenario 2: Direct Weather Report**
    *   **User:** "What's the weather like in London tomorrow?"
    *   **Expected Kai:** Provides a summary of the weather in London.
*   [ ] **Scenario 3: Full Planning Flow & Confirmation**
    *   **User:** "Find a good time for a 2-hour bike ride in Paris this weekend."
    *   **Expected Kai:** Proposes the best time for a bike ride based on the weather.
    *   **User:** "Yes, that sounds perfect. Please schedule it."
    *   **Expected Kai:** Creates a Google Calendar event and confirms with the user.
*   [ ] **Scenario 4: Session Management**
    *   Complete Scenario 3.
    *   Start a new conversation.
    *   **User:** "How's the weather here?"
    *   **Expected Kai:** Asks for the city again.

## 6. Confidence Score

10/10 - The plan is comprehensive, well-researched, and based on proven patterns from both internal and external sources.
