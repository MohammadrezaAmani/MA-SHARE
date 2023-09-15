"""
include download routes
"""
from fastapi import APIRouter, UploadFile
from fastapi.responses import RedirectResponse
from fastapi import File
from mashare.utils.utils import conf

router = APIRouter(
    prefix="/upload",
    tags="upload",
    default_response_class={404: {"message": "not found"}},
)


@router.post("/{file_path:path}")
async def create_upload_file(
    file_path: str = File(description="A file path"),
    file: UploadFile = File(description="A file read as UploadFile"),
):
    "upload files to computer"
    if file_path.startswith("//"):
        file_path = file_path[1:]
    with open(file_path + "/" + file.filename, "wb") as buffer:
        ip, port = conf()
        buffer.write(file.file.read())
    url = f"http://{ip}:{port}{file_path}"
    return RedirectResponse(
        url=url,
        status_code=303,
    )
