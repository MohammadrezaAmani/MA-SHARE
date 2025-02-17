"photo router"

from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from mashare import BASE_PATH

# from mashare.templates.templates import template
from mashare.templates.photo import photo

router = APIRouter(
    prefix="/photo",
    tags=["photo"],
    default_response_class={404: {"message": "not found"}},
)
router.mount(BASE_PATH + "/assets", StaticFiles(directory="assets"), name="assets")


@router.get("/{file_path:path}")
async def video_play(file_path: str):
    "main router"
    return HTMLResponse(photo("/" + file_path))
