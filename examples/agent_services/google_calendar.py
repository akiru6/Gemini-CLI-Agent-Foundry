import uuid
from googleapiclient.discovery import build
from src.models import ActivityWindow


class GoogleCalendarService:
    def __init__(self, credentials):
        self.service = build("calendar", "v3", credentials=credentials)

    def create_event(self, window: ActivityWindow, activity: str) -> str:
        event_id = f"activityadv{uuid.uuid4().hex}"
        event_body = {
            "summary": f"🗓️ Recommended time for {activity}",
            "description": window.summary,
            "start": {
                "dateTime": window.start_time.isoformat(),
                "timeZone": "auto",
            },
            "end": {
                "dateTime": window.end_time.isoformat(),
                "timeZone": "auto",
            },
            "id": event_id,
        }
        self.service.events().insert(calendarId="primary", body=event_body).execute()
        return event_id

    def get_event(self, event_id: str):
        return (
            self.service.events().get(calendarId="primary", eventId=event_id).execute()
        )

    def delete_event(self, event_id: str):
        self.service.events().delete(calendarId="primary", eventId=event_id).execute()
