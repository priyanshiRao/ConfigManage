from fastapi import FastAPI
from app.routers import config
from app.database import engine, Base

# Create the database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include the configuration router
app.include_router(config.router)
