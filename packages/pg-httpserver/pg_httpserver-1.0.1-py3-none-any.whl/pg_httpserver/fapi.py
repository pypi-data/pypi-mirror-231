import asyncio

from fastapi import FastAPI, Query, Request
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from pg_common import log_info
from pg_environment import config, ENV_HOSTIP, ENV_HOSTPORT, ENV_DEBUG
import io


__all__ = [
           "run",
           ]
__auth__ = "baozilaji@gmail.com"


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/configInfo")
async def config_info():
    return '{"maintenance": {}, "announce_client": {}'


@app.post("/h5protocol")
async def handle(*, player_id: int = Query(..., alias="playerId"), req: Request):
    log_info(player_id)
    log_info(req)
    _r_data = "ok"
    _stream = io.BytesIO(_r_data.encode())
    return StreamingResponse(_stream, media_type="application/octet-stream")


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
    uvicorn.run(app="pg_httpserver.fapi:app", host=config.get_conf(ENV_HOSTIP),
                port=config.get_conf(ENV_HOSTPORT))