import os
from fastapi import FastAPI, Header, HTTPException
from openai import OpenAI

app = FastAPI()

# DigitalOcean Inference Endpoint
# Set AGENT_ENDPOINT in App Platform Env Vars
client = OpenAI(
    base_url=os.getenv("DO_INFERENCE_ENDPOINT") + "/api/v1/",
    api_key=os.getenv("DO_INFERENCE_TOKEN")
)

@app.post("/generate-header")
async def generate_header(prompt: str, x_api_key: str = Header(...)):
    if x_api_key != os.getenv("CLI_TOKEN"):
        raise HTTPException(status_code=403, detail="Unauthorized")
    
    # Generate image using DO Inference Engine
    response = client.images.generate(
        model="dall-e-3", # Use your catalog-supported model
        prompt=f"Absurdist digital painting style: {prompt}",
        n=1,
        size="1024x1024"
    )
    return {"image_url": response.data[0].url}
