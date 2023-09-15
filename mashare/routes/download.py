"""
include download routes
"""
import os
import mimetypes
from fastapi import APIRouter
from fastapi.responses import StreamingResponse, FileResponse

router = APIRouter(
    prefix="/dl/",
    tags="Download",
    default_response_class={404: {"message": "not found"}},
)


@router.get("/{file_path:path}")
async def read_file_dl(file_path: str):
    "for downloading files"
    file_path = "/" + file_path
    media_type = mimetypes.guess_type(file_path)[0]
    file = open(file_path, "rb")
    if os.path.getsize(file_path) > 10000:
        return StreamingResponse(
            file,
            media_type=media_type,
            headers={
                "Content-Disposition": f"attachment; filename={file_path.rsplit('/', 1)[1]}"
            },
        )
    else:
        return FileResponse(file_path)
