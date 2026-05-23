from fastapi import FastAPI, Header, HTTPException
import fal_client
import os

app = FastAPI()

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/generate")
async def generate_image(text: str, x_api_key: str = Header(...)):
    # Validate the token sent by your CLI
    if x_api_key != os.getenv("CLI_TOKEN"):
        raise HTTPException(status_code=403, detail="Unauthorized")
    
    # Generate image via Fal
    handler = fal_client.submit(
        "fal-ai/flux/schnell",
        arguments={"prompt": f"Absurdist digital painting: {text[:200]}"}
    )
    result = handler.get()
    return {"image_url": result['images'][0]['url']}
