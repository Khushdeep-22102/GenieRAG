from fastapi import FastAPI
from pydantic import BaseModel
from generate_response import generate_response

app = FastAPI()

class QueryRequest(BaseModel):
    query: str

@app.post("/ask")
async def ask_question(request: QueryRequest):
    """API endpoint to get answers from the LLM."""
    response = generate_response(request.query)
    return {"query": request.query, "response": response}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
