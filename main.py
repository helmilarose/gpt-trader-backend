from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.openapi.utils import get_openapi
import openai
import os

app = FastAPI()
openai.api_key = os.getenv("OPENAI_API_KEY")

class SignalRequest(BaseModel):
    context: str

@app.post("/generate-signal")
async def generate_signal(req: SignalRequest):
    prompt = f"""
    Tu es un expert en trading algorithmique. Analyse le contexte suivant et génère un signal clair :

    {req.context}

    Réponds par : BUY, SELL ou WAIT avec une justification concise.
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    signal = response['choices'][0]['message']['content']
    return {"signal": signal}

@app.get("/openapi.json")
def get_open_api_endpoint():
    return get_openapi(
        title="GPT-Trader-Pro Actions",
        version="1.0.0",
        description="Génère un signal de trading basé sur un contexte",
        routes=app.routes,
    )
