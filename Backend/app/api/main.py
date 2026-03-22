from fastapi import FastAPI
from app.api.routes import chat, admin, session

app = FastAPI(
    title="University Policy Assistant API",
    version="1.0.0"
)

app.include_router(chat.router)
app.include_router(admin.router)
app.include_router(session.router)