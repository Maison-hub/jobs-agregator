import os
import json

from llama_cpp import Llama

# Chemin absolu vers le modèle
MODEL_PATH = os.path.abspath("app/models/phi-2.Q3_K_S.gguf")

SYSTEM_MESSAGE = """
You are a helpful assistant.
You provide ratings indicating the match between a job posting and a candidate's profile.
The rating should be a number between 0 and 100.
"""

# Utilisez un format de chat valide
llm = Llama(model_path=MODEL_PATH, chat_format="chatml-function-calling", n_ctx=2048, n_threads=8, n_batch=512, max_tokens=50)

# def ask_llm(question, functions, tool_choice):
#     return llm.create_chat_completion(
#         messages=[
#             {"role": "system", "content": SYSTEM_MESSAGE},
#             {"role": "user", "content": question}
#         ],
#         tools=functions,
#         tool_choice={"type": "function", "function": {"name": tool_choice}}
#     )

def evaluate_offer(job_description: str, user_description: str):
    prompt = f"""
    Profil de l'utilisateur : {user_description}
    
    Offre d'emploie : {job_description}
    """

    tools = [
        {
            "type": "function",
            "function" : {
                "name": "evaluate_offer",
                "parameters": {
                    "type": "object",
                    "title": "Evaluation de l'offre",
                    "properties": {
                        "match_score":
                            {
                                "title": "Corresponding score between 0 and 100",
                                "type": "integer",
                            }
                    },
                    "required": ["match_score"]
                }
            }
        }
    ]

    response = llm.create_chat_completion(
        messages=[
            {"role": "system", "content": SYSTEM_MESSAGE},
            {"role": "user", "content": prompt}
        ],
        tools=tools,
        tool_choice={"type": "function", "function": {"name": "evaluate_offer"}}
    )

    # # Extraire uniquement un chiffre
    # score = ''.join(filter(str.isdigit, response))
    #
    # if not score:
    #     raise HTTPException(status_code=500, detail="L'IA n'a pas retourné de score valide")
    print(os.cpu_count())
    function_call = response["choices"][0]["message"]["tool_calls"][0]['function']
    arg = json.loads(function_call["arguments"])
    score = arg.get("match_score")
    print(response)
    return score