## FEATURE:

Build the **"Kai" Conversational Weather Advisor**, an interactive web application that acts as a personal assistant for planning and understanding weather-dependent activities.

The application will feature a **dialog-based chat interface** where a user can have an ongoing conversation with Kai.

## Core Conversational Capabilities:

1.  **Conversational Planning (Kai's "Analyst" Skill):**
    -   The user can ask Kai to plan an activity in natural language (e.g., "I want to have a picnic in Paris this weekend").
    -   Kai must first gather all relevant weather data for the request.
    -   Kai must then **analyze the raw data** and present a **reasoned recommendation** to the user. The response should not be a simple "yes" or "no," but a helpful summary (e.g., "The evening of Sunday looks best because the wind will be calm...").
    -   The proposal must end with a clear question to the user, asking for confirmation to schedule the event.

2.  **Direct Weather Queries:**
    -   The user can ask for a simple weather report (e.g., "What's the weather like in London tomorrow?").
    -   Kai will gather the hourly data and **synthesize it into a human-friendly paragraph**, highlighting key information like temperature ranges, precipitation, and wind.

3.  **Slot-Filling Dialogue:**
    -   If the user's request is missing critical information (like the city), Kai **must not fail**.
    -   Kai must ask a friendly, clarifying question to "fill the slot" (e.g., "That sounds lovely! Which city are you in?").

4.  **Action Confirmation:**
    -   Kai **must never** perform an action (like creating a calendar event) without first receiving explicit confirmation from the user (e.g., "Yes, please schedule that.").

5.  **Conversational Memory:**
    -   Kai must remember the context of the current conversation, especially the location being discussed, to handle multi-turn requests gracefully.

## Technical Dependencies:

-   A capable LLM (e.g., Google Gemini) for reasoning.
-   A weather data provider (e.g., Open-Meteo).
-   Google Calendar API for scheduling.
-   A web framework (e.g., Streamlit) for the user interface.
-   A session management system to handle distinct conversations.