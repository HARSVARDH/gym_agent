from langchain_core.tools import tool
from memory import get_last_workout

@tool
def get_calendar_events(date: str) -> str:
    """Return today's calendar events."""
    return """
4:00 pm - Class
1:30 PM - Lunch
7:30 PM - Dinner
"""

@tool
def get_meal_times() -> str:
    """Return user's meal schedule."""
    return """
Breakfast: 8:30 am to 9:30 am
Lunch: 1:30 pm to 2:15 pm 
Dinner: 7:30 pm to 8:15 pm 
"""

@tool
def get_last_workout_tool() -> str:
    """Return last workout for recovery planning."""
    return get_last_workout()