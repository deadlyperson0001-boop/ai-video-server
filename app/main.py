from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
from app.auth import verify_key

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def home():
    return {"status": "AI server running"}

@app.post("/chat")
def chat(request: ChatRequest, x_api_key: str = Header(None)):

    if not verify_key(x_api_key):
        raise HTTPException(status_code=403, detail="Invalid API key")

    user_message = request.message

    response = f"AI received your message: {user_message}"

    return {
        "reply": response
    }
