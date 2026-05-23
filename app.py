import os
import requests
from fastapi import FastAPI, Header, HTTPException
from openai import OpenAI

app = FastAPI()

# DigitalOcean Inference Client
client = OpenAI(
    base_url="https://inference.do-ai.run/v1",
    api_key=os.getenv("DO_API_TOKEN") 
)

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/generate")
async def generate_image(prompt: str, x_api_key: str = Header(...)):
    # Validate your custom CLI token
    if x_api_key != os.getenv("CLI_TOKEN"):
        raise HTTPException(status_code=403, detail="Unauthorized")
    
    try:
        # Request generation from DO Native Inference
        response = client.images.generate(
            model="stable-diffusion-3.5-large",
            prompt=f"Absurdist digital painting style: {prompt}",
            n=1,
            size="1024x1024"
        )
        return {"image_url": response.data[0].url}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
