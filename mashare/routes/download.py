"""
include download routes
"""

import os

from fastapi import APIRouter
from fastapi.responses import StreamingResponse

router = APIRouter(
    prefix="/dl",
    tags=["Download"],
    default_response_class={404: {"message": "not found"}},
)


@router.get("/{file_path:path}")
def read_file_dl(file_path: str):
    "for downloading files"
    file_path = "/" + file_path
    file_size = os.path.getsize(file_path)

    def generate():
        with open(file_path, "rb") as file:
            while True:
                chunk = file.read(65536)  # Adjust the chunk size as needed
                if not chunk:
                    break
                yield chunk

    return StreamingResponse(
        content=generate(),
        media_type="application/octet-stream",
        headers={
            "Content-Disposition": f"attachment; filename={file_path.rsplit('/', 1)[1].encode('utf-8').decode('latin-1')}",
            "Content-Length": str(file_size),
        },
    )
