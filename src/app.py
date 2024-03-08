import uvicorn
from container import init_container, shutdown_container
from fastapi import FastAPI
from routes.router import router
from starlette.applications import Starlette
from starlette.routing import Mount

fast_api_app = FastAPI()

fast_api_app.include_router(router)

app = Starlette(routes=[Mount("/api/thirdplace", fast_api_app)])


@app.on_event("startup")
def start_application():
    init_container()


@app.on_event("shutdown")
def shutdown_event():
    shutdown_container()


if __name__ == "__main__":
    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        port=12121,
        log_level="info",
        reload=True,
    )
