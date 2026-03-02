# Gym Scheduler Agent 🏋️‍♂️🤖

**A personal AI agent that suggests the best time for you to go to the gym based on your schedule, meal times, and past workouts.**  

Built using **LangChain v1+**, **LangGraph**, and **Chroma** for long-term memory.

---

## Features 

- ✅ Suggests gym time based on **mock Google Calendar events**  
- ✅ Takes into account **meal times**  
- ✅ Remembers your **past workouts** using **Chroma vector DB**  
- ✅ Explains reasoning using **ReAct reasoning loop**  
- ✅ API endpoint via **FastAPI** (`/gym-time`)  

---

## How It Works

1. The agent queries:
   - Calendar events (currently mocked)  
   - Meal times (mocked JSON)  
   - Last workout from memory (Chroma)  

2. The **ReAct agent** decides:
   - Which time block is free  
   - Recovery timing (e.g., 48h for same muscle group)  
   - Suggests the best gym slot  

3. The user can **confirm workout**, which is then saved to memory.

---

Future Development Ideas
- Real Google Calendar integration – Pull actual events to suggest gym times dynamically.
- Planet Fitness or wearable integration – Track past workouts, steps, or heart rate for personalized suggestions.
- Muscle group tracking – Remember last workout type (push/pull/legs) for recovery planning.
- Analytics dashboard – Track streaks, progress, and agent recommendations over time.
---
