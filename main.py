from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from pydantic import BaseModel, HttpUrl
import string
import random

app = FastAPI(title="Simple URL Shortener")

# In-memory storage
url_db = {}

class URLRequest(BaseModel):
    long_url: HttpUrl


def generate_short_code(length: int = 6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))


@app.post("/shorten")
def shorten_url(data: URLRequest):
    short_code = generate_short_code()
    url_db[short_code] = data.long_url
    return {
        "short_url": f"http://127.0.0.1:8000/{short_code}",
        "original_url": data.long_url
    }


@app.get("/{short_code}")
def redirect_url(short_code: str):
    if short_code not in url_db:
        raise HTTPException(status_code=404, detail="URL not found")
    return RedirectResponse(url_db[short_code])
