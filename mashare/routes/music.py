"main router"

from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

# from mashare.templates.templates import template
from mashare.templates.music import music
from mashare import BASE_PATH

router = APIRouter(
    prefix="/audio",
    tags=["audio"],
    default_response_class={404: {"message": "not found"}},
)
router.mount(BASE_PATH + "/assets", StaticFiles(directory="assets"), name="assets")


@router.get("/{file_path:path}")
async def music_play(file_path: str):
    "main router"
    return HTMLResponse(music("/" + file_path))
