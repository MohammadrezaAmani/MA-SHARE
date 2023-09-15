"main router"

from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
# from mashare.templates.templates import template
from mashare.templates.base import base
from mashare import BASE_PATH

router = APIRouter(
    prefix="/show",
    tags=["show"],
    default_response_class={404: {"message": "not found"}},
)
router.mount(BASE_PATH+"/assets", StaticFiles(directory="assets"), name="assets")

@router.get("/{file_path:path}")
async def main_router(file_path: str):
    "main router"
    return HTMLResponse(base('/'+file_path))
