from fastapi import FastAPI
from netlify.functions import custom_badge
from fastapi.staticfiles import StaticFiles

from netlify.functions import badge

app = FastAPI()

app.mount("/static/icons", StaticFiles(directory="icons"), name="icons")
app.include_router(custom_badge.router)
app.include_router(badge.router)


@app.get("/")
async def root():
    return {"message": "Hello from the Main App"}