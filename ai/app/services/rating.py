from ollama import chat
from ollama import ChatResponse

#add tool to pas to ai to return score
def get_score(score: int):
    """
    return the score of correspondence between job offer and user profile from 0 to 100
    :arg score: int
    :return: score
    """
    return score

def evaluate_offer(job_description: str, user_description: str):
    """
    Evaluate the correspondence between a job offer and a user profile
    :arg job_description: str
    :arg user_description: str
    :return: score
    """
    prompt = f"""
    You are an assistant who evaluates the correspondence between a job offer and a user profile.
    Give only a score out of 100.

    Profile: {user_description}
    Offer: {job_description}

    Response:
    """

    response = chat(prompt)

    # Extract only a number
    score = ''.join(filter(str.isdigit, response))

    if not score:
        raise Exception("The AI did not return a valid score")

    return int(score)


# from llama_cpp import Llama
#
# #add here ai model to evaluate offer
# MODEL_PATH = "/app/models/mistral-7b-instruct.Q5_K_M.gguf"
# SYSTEM_MESSAGE="""
# You are a helpful assistant.
# You can call functions with appropriate input when necessary
# """
# llm = Llama(model_path=MODEL_PATH, chat_format="chatlm-function-calling")
#
# def ask_llm(question, functions, tool_choice):
#     return llm.create_chat_completion(
#         messages = [
#             {"role": "system", "content": SYSTEM_MESSAGE},
#             {"role": "user", "content": question}
#         ],
#         tools=functions,
#         tool_choice={ "type": "function", "function": {"name": tool_choice}})
#
# def evaluate_offer(job_description: str, user_description: str):
#     prompt = f"""
#     Tu es un assistant qui évalue la correspondance entre une offre d'emploi et un profil utilisateur.
#     Donne uniquement un score sur 100.
#
#     Profil : {profile}
#     Offre : {job_offer}
#
#     Réponse :
#     """
#
#     functions = [
#         {
#             "name": "evaluate_offer",
#             "description": "Évalue la correspondance entre une offre d'emploi et un profil utilisateur.",
#             "parameters": {
#                 "type": "object",
#                 "properties": {
#                     "match_score": {"type": "integer", "description": "Score de correspondance sur 100"}
#                 },
#                 "required": ["match_score"]
#             }
#         }
#     ]
#
#     response = ask_llm(prompt, functions, "match_score")
#
#     # Extraire uniquement un chiffre
#     score = ''.join(filter(str.isdigit, response))
#
#     if not score:
#         raise HTTPException(status_code=500, detail="L'IA n'a pas retourné de score valide")
#
#     return {"score": int(score)}