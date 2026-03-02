from fastapi import FastAPI
from agent import run_agent

app = FastAPI()

@app.get("/gym-time")
async def get_gym_time():
    result = run_agent("When should I go to the gym today?")
    return {"suggestion": result}