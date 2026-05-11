from fastapi import FastAPI
from src.api import custom_badge, badge
from fastapi.staticfiles import StaticFiles

app = FastAPI(redoc_url=None, docs_url="/", title="BadgeLab", version="1.0.0", swagger_ui_parameters={})


app.mount("/static/icons", StaticFiles(directory="src/icons"), name="icons")
app.include_router(custom_badge.router)
app.include_router(badge.router)
