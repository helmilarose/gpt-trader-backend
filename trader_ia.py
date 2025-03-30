from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import openai
import os

app = FastAPI()

class SignalRequest(BaseModel):
    context: str

@app.post("/generate-signal")
async def generate_signal(request: SignalRequest):
    try:
        print("✅ Requête reçue :", request.context)

        openai.api_key = os.getenv("OPENAI_API_KEY")

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "user", "content": request.context}
            ]
        )

        signal = response.choices[0].message["content"]
        return {"signal": signal}

    except Exception as e:
        print("❌ Erreur dans generate_signal :", e)
        raise HTTPException(status_code=500, detail=str(e))
