import os
import requests
from fastapi import FastAPI, Header, HTTPException

app = FastAPI()

DO_INFERENCE_URL = "https://inference.do-ai.run/v1/async-invoke"
DO_API_TOKEN = os.getenv("DO_API_TOKEN")

@app.post("/generate")
async def generate_image(prompt: str, x_api_key: str = Header(...)):
    if x_api_key != os.getenv("CLI_TOKEN"):
        raise HTTPException(status_code=403, detail="Unauthorized")
    
    # Submit the job to DigitalOcean Inference
    response = requests.post(
        DO_INFERENCE_URL,
        headers={"Authorization": f"Bearer {DO_API_TOKEN}", "Content-Type": "application/json"},
        json={
            "model_id": "fal-ai/flux/schnell", # Or your preferred model
            "input": {"prompt": f"Absurdist digital painting: {prompt}"}
        }
    )
    
    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Inference API error")
        
    return response.json() # Returns the request_id and status
