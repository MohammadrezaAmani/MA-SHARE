"main router"

from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from mashare.templates.templates import template

router = APIRouter(
    prefix="/show",
    tags="show",
    default_response_class={404: {"message": "not found"}},
)


@router.get("/{file_path:path}")
async def main_router(file_path: str):
    "main router"
    return HTMLResponse(template(file_path))
