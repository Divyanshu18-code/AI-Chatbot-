# Step 1: Setup Pydantic model (schema validation)
from pydantic import BaseModel
from typing import List


class RequestState(BaseModel):
    model_name: str
    system_prompt: str
    messages: List[str]
    allow_search: bool


# Step 2: Setup AI Agent from frontend request
from fastapi import FastAPI
from ai_agent import get_response_from_ai_agent

ALLOWED_MODEL_NAMES = ["llama-3.3-70b-versatile", "llama-3.1-8b-instant"]

app = FastAPI(title="LangGraph AI Agent")


@app.post("/chat")
def chat_endpoint(request: RequestState):
    """
    API Endpoint to interact with the Chatbot using LangGraph and search tools.
    It dynamically selects the model specified in the request.
    """
    if request.model_name not in ALLOWED_MODEL_NAMES:
        return {"error": "Invalid model name. Kindly select a valid AI model."}

    llm_id = request.model_name
    query = request.messages[-1]
    allow_search = request.allow_search
    system_prompt = request.system_prompt

    # Create AI Agent and get response
    response = get_response_from_ai_agent(llm_id, query, allow_search, system_prompt)
    return response


# Step 3: Run app & explore Swagger UI docs
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=9999)


