"""
include download routes
"""
import os
import shutil
from fastapi import APIRouter, UploadFile, File
from fastapi.responses import RedirectResponse
from mashare.templates.utils import link_maker
router = APIRouter(
    prefix="/upload",
    tags=["upload"],
    default_response_class={404: {"message": "not found"}},
)



@router.post("/{file_path:path}")
async def create_upload_files(file_path: str, files):
    "to handle uploaded files"
    file_path = '/' + file_path
    print(file_path)
    if not os.path.exists(file_path):
        os.makedirs(file_path)

    for file in files:
        dest = os.path.join(file_path, file.filename)
        print(dest)

        with open(dest, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

    return RedirectResponse(url=link_maker(file_path,'show'), status_code=303)