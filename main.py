"""FastAPI File Sharing By Mohammadreza Amani"""
# ------------- Imports -------------
import os
import uvicorn
import mimetypes
from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import (
    StreamingResponse,
    RedirectResponse,
    FileResponse,
)
from FileShare import (
    template,
    videoPlayer,
    textEditore_template,
    musicPlayer,
    generate_qr_code,
    IP,
    PORT,
)

# creating main FastAPI object
app = FastAPI()

print(f"Server is running on http://{IP}:{PORT}")


# -------------- Routes --------------

# text editor
@app.post("/textEditor/")
async def textEditor(file_path: str = Form(...), file_content: str = Form(...)):
    with open(file_path, "w") as f:
        f.write(file_content)
    back = file_path.rsplit("/", 1)[0]
    return RedirectResponse(
        url=f"http://{IP}:{PORT}{back}",
        status_code=303,
    )


# upload file
@app.post("/uploadfile/")
async def create_upload_file(
    file_path: str = File(description="A file path"),
    file: UploadFile = File(description="A file read as UploadFile"),
):
    if file_path.startswith("//"):
        file_path = file_path[1:]
    with open(file_path + "/" + file.filename, "wb") as buffer:
        buffer.write(file.file.read())
    url = f"http://{IP}:{PORT}{file_path}"
    return RedirectResponse(
        url=url,
        status_code=303,
    )


# download file
def download(file_path: str) -> StreamingResponse:
    """download file

    Args:
        file_path (str): path of the file

    Returns:
        StreamingResponse: file response
    """
    file = open(file_path, "rb")
    if os.path.getsize(file_path) > 100000000:
        return StreamingResponse(
            file,
            headers={
                "Content-Disposition": f"attachment; filename={file_path.rsplit('/', 1)[1]}"
            },
        )
    return FileResponse(file_path)


# show file: text, music, video
@app.get("/dl/{file_path:path}")
def read_file_dl(file_path: str):
    file_path = "/" + file_path
    media_type = mimetypes.guess_type(file_path)[0]
    if media_type.startswith("text"):
        return textEditore_template(file_path)
    if media_type.startswith("audio"):
        return musicPlayer(file_path)
    if media_type.startswith("video"):
        return videoPlayer(file_path)
    file = open(file_path, "rb")
    if os.path.getsize(file_path) > 100000000:
        return StreamingResponse(
            file,
            media_type=media_type,
            headers={
                "Content-Disposition": f"attachment; filename={file_path.rsplit('/', 1)[1]}"
            },
        )
    else:
        return FileResponse(file_path)


# main route
@app.get("{file_path:path}")
def read_file(file_path: str):
    if not os.path.exists(file_path):
        return {"status_code": 404}
    if not os.path.isdir(file_path):
        return download(file_path)

    return template(file_path)


# -------------- Main --------------
if __name__ == "__main__":
    generate_qr_code()
    print("Server Started")
    uvicorn.run(app, host=IP, port=PORT, log_level="error")
