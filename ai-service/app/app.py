from fastapi import FastAPI
from pydantic import BaseModel
from .services import evaluate_offer

app = FastAPI()

class OfferEvaluationRequest(BaseModel):
    job_description: str
    user_description: str

class OfferEvaluationResponse(BaseModel):
    score: int  # Un nombre entre 0 et 100

@app.post("/evaluate-offer", response_model=OfferEvaluationResponse)
async def evaluate_offer_route(request: OfferEvaluationRequest):
    score = evaluate_offer(request.job_description, request.user_description)
    return {"score": score}
