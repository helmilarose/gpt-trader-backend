import os
from dotenv import load_dotenv
from trader_ia import generate_signal_from_gpt

load_dotenv()

# Données de test simulées
context = """
Actif : EUR/USD
Prix actuel : 1.0930
RSI (14) : 72
MACD : croisement haussier
Moyenne mobile 50 vs 200 : Golden Cross détecté
Volume en hausse de 20% sur 3 jours
"""

signal = generate_signal_from_gpt(context)
print("✅ Signal généré par GPT-Trader-Pro :", signal)
