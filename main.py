from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import create_tables, drop_tables
from router import router as tasks_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    pass
    # # Load the ML model
    await drop_tables()
    print("--------Base data tables dropped-------")
    await create_tables()
    print("=======DataBase redy=========")
    yield
    # # Clean up the ML models and release the resources
    print("Aus")






app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)

@app.get("/")
def get_home():
    return {"hello" : "world"}




