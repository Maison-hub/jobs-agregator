from llama_cpp import Llama

#add here ai model to evaluate offer
MODEL_PATH = "/app/models/mistral-7b-instruct.Q5_K_M.gguf"
SYSTEM_MESSAGE="""
You are a helpful assistant.
You can call functions with appropriate input when necessary
"""
llm = Llama(model_path=MODEL_PATH, chat_format="chatlm-function-calling")

def ask_llm(question, functions, tool_choice):
    return llm.create_chat_completion(
        messages = [
            {"role": "system", "content": SYSTEM_MESSAGE},
            {"role": "user", "content": question}
        ],
        tools=functions,
        tool_choice={ "type": "function", "function": {"name": tool_choice}})

def evaluate_offer(job_description: str, user_description: str):
    prompt = f"""
    Tu es un assistant qui évalue la correspondance entre une offre d'emploi et un profil utilisateur.
    Donne uniquement un score sur 100.

    Profil : {profile}
    Offre : {job_offer}

    Réponse : 
    """

    functions = [
        {
            "name": "evaluate_offer",
            "description": "Évalue la correspondance entre une offre d'emploi et un profil utilisateur.",
            "parameters": {
                "type": "object",
                "properties": {
                    "match_score": {"type": "integer", "description": "Score de correspondance sur 100"}
                },
                "required": ["match_score"]
            }
        }
    ]

    response = ask_llm(prompt, functions, "match_score")

    # Extraire uniquement un chiffre
    score = ''.join(filter(str.isdigit, response))

    if not score:
        raise HTTPException(status_code=500, detail="L'IA n'a pas retourné de score valide")

    return {"score": int(score)}