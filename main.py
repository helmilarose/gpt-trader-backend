from fastapi import FastAPI
from pydantic import BaseModel
import openai
import os

app = FastAPI()

# Configuration de la clé API - Version sécurisée
openai.api_key = os.environ.get("OPENAI_API_KEY")  # Utilisation de environ.get pour plus de robustesse

class SignalRequest(BaseModel):
    context: str

@app.post("/generate-signal")
async def generate_signal(req: SignalRequest):
    try:
        # Vérification renforcée de la clé API
        if not openai.api_key:
            return {"error": "Configuration manquante", "solution": "Vérifiez OPENAI_API_KEY dans Render"}

        # Prompt optimisé pour GPT-4
        prompt = f"""Format de réponse obligatoire :
Action: BUY/SELL/WAIT
Raison: (2 mots maximum)
Contexte: {req.context}"""

        # Appel API sécurisé avec timeout
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {
                    "role": "system",
                    "content": "Tu es un trader expert. Réponds uniquement par : Action: [BUY/SELL/WAIT] Raison: [2 mots]"
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.1,  # Précis mais pas rigide
            max_tokens=20,
            request_timeout=15  # Timeout explicite
        )

        # Nettoyage et validation de la réponse
        raw_content = response.choices[0].message['content']
        cleaned_content = raw_content.replace("\n", " ").strip()
        return {"signal": cleaned_content}

    except openai.error.AuthenticationError:
        return {"error": "Clé API invalide", "solution": "Vérifiez OPENAI_API_KEY dans Render"}
    except Exception as e:
        return {"error": "Erreur de traitement", "details": str(e)}