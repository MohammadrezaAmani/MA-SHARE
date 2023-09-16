"main router"

from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

# from mashare.templates.templates import template
from mashare.templates.file_table import file_table
from mashare import BASE_PATH
from mashare.data import cache

router = APIRouter(
    prefix="/show",
    tags=["show"],
    default_response_class={404: {"message": "not found"}},
)
router.mount(BASE_PATH + "/assets", StaticFiles(directory="assets"), name="assets")


@router.get("/{file_path:path}")
async def main_router(file_path: str):
    "main router"
    cached_html = cache.check("/" + file_path)
    if cached_html:
        return HTMLResponse(cached_html)
    html = file_table("/" + file_path)
    cache.add("/" + file_path, html)
    return HTMLResponse(html)
