import uuid
from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.responses import RedirectResponse
from fastapi import HTTPException

app = FastAPI()

class URLRequest(BaseModel):
    url: str

url_mapping = {}

@app.get("/")
def read_root():
    return{"message": "Starting URL Shortener"}

@app.get("/{short_id}")
def redirect_to_url(short_id: str):
    if short_id in url_mapping:
        long_url = url_mapping[short_id]
        return RedirectResponse(long_url)
    
    else:

        raise HTTPException(status_code = 404, detail = "Short URL not found")


@app.post("/shorten")   
def create_short_url(request_data: URLRequest, request: Request):
    long_url = request_data.url
    short_id = uuid.uuid4().hex[:6]

    url_mapping[short_id] = long_url

    base_url = str(request.base_url)
    short_url = base_url + short_id

    return {"short_url": short_url}
