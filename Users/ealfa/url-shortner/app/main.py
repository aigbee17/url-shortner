import uuid
from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.responses import RedirectResponse
from fastapi import HTTPException
from app.database import SessionLocal, URL
from sqlalchemy.orm import Session
from fastapi import Depends
from app.database import Base, engine
Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI()

class URLRequest(BaseModel):
    url: str

url_mapping = {}

@app.get("/")
def read_root():
    return{"message": "Starting URL Shortener"}

@app.get("/{short_id}")
def redirect_to_url(short_id: str, db: Session = Depends(get_db)):
    result = db.query(URL).filter(URL.short_id == short_id).first()
    if result:
        result.clicks += 1
        db.commit()
        return RedirectResponse(result.original_url)
    
    else: 

        raise HTTPException(status_code = 404, detail = "Short URL not found")


@app.post("/shorten")   
def create_short_url(
    request_data: URLRequest, 
    request: Request,
    db: Session = Depends(get_db)
):

    long_url = request_data.url
    short_id = uuid.uuid4().hex[:6]

    db_url = URL(short_id=short_id, original_url=long_url)
    db.add(db_url)
    db.commit()

    url_mapping[short_id] = long_url

    
    short_url = str(request.base_url) + short_id
    return {"short_url": short_url}



@app.get("/stats/{short_id}")
def get_click_stats(short_id: str, db: Session = Depends(get_db)):
    result = db.query(URL).filter(URL.short_id == short_id).first()
    if result:
        return{
            "short_id": result.short_id,
            "original_url": result.original_url,
            "clicks": result.clicks
        }
    
    else:
        raise HTTPException(status_code = 404, detail= "Short URL not found")
