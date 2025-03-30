import requests

url = "https://gpt-trader-backend.onrender.com/generate-signal"

headers = {
    "Content-Type": "application/json"
}

data = {
    "context": "Analyse du marché USD/JPY avec signaux techniques RSI et MACD"
}

response = requests.post(url, headers=headers, json=data)

print("Status code:", response.status_code)
print("Réponse brute :", response.text)  # <-- Affiche le contenu exact de l'erreur
