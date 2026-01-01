from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import stations, routes

app = FastAPI(title="SPUF-314 BMTC Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(stations.router)
app.include_router(routes.router)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000)
