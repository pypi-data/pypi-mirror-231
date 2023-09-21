from fastapi import FastAPI
import uvicorn
from pg_common import log_info
from pg_environment import config


app = FastAPI()


@app.middleware("http")
async def http_inspector(request, call_next):
    response = await call_next(request)
    return response


@app.on_event("startup")
async def startup():
    log_info("http server startup")


@app.on_event("shutdown")
async def shutdown():
    log_info("http server shutdown")


def run():
    uvicorn.run(app="pg_httpserver.fapi:app")