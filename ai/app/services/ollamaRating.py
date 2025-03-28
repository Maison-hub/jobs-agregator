import os
import json
import ollama
from ollama import chat
from ollama import ChatResponse
from ollama import Client

MODEL_NAME = "mistral"

SYSTEM_MESSAGE = """
You are a helpful assistant.
You provide ratings indicating the match between a job posting and a candidate's profile.
The rating should be a number between 0 and 100.
"""

def evaluate_offer(job_description: str, user_description: str):
    client = Client(
        host='http://host.docker.internal:11434',
    )

    prompt = f"""
    Profil de l'utilisateur : {user_description}
    
    Offre d'emploi : {job_description}
    
    Donne un score de correspondance entre 0 et 100 sous le format JSON suivant :
    {{"match_score": <valeur>}}
    """

    response: ChatResponse = client.chat(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": SYSTEM_MESSAGE},
            {"role": "user", "content": prompt}
        ]
    )

    try:
        result = json.loads(response["message"]["content"])
        return result.get("match_score", 0)
    except (json.JSONDecodeError, KeyError):
        return 0
