import os
from fastapi import FastAPI, Header, HTTPException
from openai import OpenAI

app = FastAPI()

# Initialize the client with the DO Inference Base URL
client = OpenAI(
    base_url="https://inference.do-ai.run/v1",
    api_key=os.getenv("DO_INFERENCE_TOKEN") # Your Model Access Key
)

@app.post("/generate")
async def generate_image(text: str, x_api_key: str = Header(...)):
    # Validate your internal CLI token
    if x_api_key != os.getenv("CLI_TOKEN"):
        raise HTTPException(status_code=403, detail="Unauthorized")
    
    # Generate image using a supported model like stable-diffusion-3.5-large
    response = client.images.generate(
        model="stable-diffusion-3.5-large",
        prompt=f"Absurdist digital painting: {text[:200]}",
        n=1,
        size="1024x1024"
    )
    
    # The response format will depend on the model; 
    # typically provides a URL or b64_json
    return {"image_url": response.data[0].url}
