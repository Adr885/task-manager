from fastapi import FastAPI

app = FastAPI(
    title="Task Manager API",
    description="A simple Task Management REST API built with FastAPI, SQLAlchemy, and PostgreSQL.",
    version="1.0.0",
)

@app.get("/")
def root():
    return {"message": "Task Manager API is running. Visit /docs for Swagger UI."}