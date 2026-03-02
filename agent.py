from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain.agents import create_agent
from dotenv import load_dotenv
load_dotenv()
import os
from tools import (
    get_calendar_events,
    get_meal_times,
    get_last_workout_tool,
)

# LLM
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0,
)

tools = [
    get_calendar_events,
    get_meal_times,
    get_last_workout_tool,
]

system_prompt = """
You are a fitness scheduling agent.

Goal:
Suggest the best time for the user to go to the gym today.

Rules:
- Avoid calendar conflicts
- Gym must be at least 1.5 hours after meals
- Check last workout for recovery (48 hours for same muscle group)
- Prefer 1–2 hour free blocks
- Explain reasoning clearly
"""

agent = create_agent(
    model=llm,
    tools=tools,
)

def run_agent(user_input: str) -> str:
    response = agent.invoke(
        {
            "messages": [
                SystemMessage(content=system_prompt),
                HumanMessage(content=user_input),
            ]
        }
    )
    return response["messages"][-1].content