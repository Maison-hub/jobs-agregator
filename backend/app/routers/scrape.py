from fastapi import APIRouter

router = APIRouter()

@router.get("/test_toute")
async def test():
    return ["hello controller world"]