"""
include download routes
"""

from fastapi import APIRouter, Form
from fastapi.responses import RedirectResponse
from mashare.utils.utils import conf

router = APIRouter(
    prefix="/edit",
    tags="Download",
    default_response_class={404: {"message": "not found"}},
)


@router.post("/text/{file_path:path}")
async def text_editor(file_path: str, file_content: str = Form(...)):
    "func for editinig text using browser"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(file_content)
    back = file_path.rsplit("/", 1)[0]
    ip, port = conf()
    return RedirectResponse(
        url=f"http://{ip}:{port}{back}",
        status_code=303,
    )
