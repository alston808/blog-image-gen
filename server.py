from fastapi import FastAPI, Header, HTTPException
import fal_client

app = FastAPI()

@app.post("/generate")
async def generate_image(text: str, x_api_key: str = Header(...)):
    if x_api_key != "DIGITALOCEAN_API_KEY":
        raise HTTPException(status_code=403, detail="Unauthorized")
    
    # Trigger the model
    handler = fal_client.submit("fal-ai/flux/schnell", arguments={"prompt": text})
    result = handler.get()
    return {"image_url": result['images'][0]['url']}
