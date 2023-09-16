"""
include download routes
"""

from fastapi import APIRouter
from fastapi.responses import HTMLResponse, RedirectResponse
from pydantic import BaseModel
from mashare.templates.text import text_editor
from mashare.templates.utils import link_maker

router = APIRouter(
    prefix="/text",
    tags=["Download"],
    default_response_class={404: {"message": "not found"}},
)


class File(BaseModel):
    content: str


@router.get("/{file_path:path}")
async def text_edit(file_path: str):
    with open("/" + file_path, "r", encoding="utf-8") as f:
        text = f.read()
    return HTMLResponse(text_editor("/" + file_path, text=text))


@router.post("/{file_path:path}")
async def save(file_path: str, file_content: File):
    with open("/" + file_path, "w", encoding="utf-8") as f:
        f.write(file_content.content)
    return RedirectResponse(link_maker(file_path.split("/")[:-1], "show"))
