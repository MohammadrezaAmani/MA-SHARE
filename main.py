"""FastAPI File Sharing By Mohammadreza Amani"""

import os
import uvicorn
import mimetypes
import subprocess
import datetime
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import (
    StreamingResponse,
    HTMLResponse,
    RedirectResponse,
    FileResponse,
)

app = FastAPI()

my_ip = subprocess.check_output(["hostname", "-I"]).decode("utf-8").split(" ")[0]
my_port = 8000
print(f"Your IP: {my_ip}")


def convert_file_size(file_size: int) -> str:
    """convert file size to human readable format

    Args:
        file_size (int): file size in bytes

    Returns:
        str: file size in human readable format
    """
    for x in ["bytes", "KB", "MB", "GB", "TB"]:
        if file_size < 1024.0:
            return "%3.1f %s" % (file_size, x)
        file_size /= 1024.0


def get_files(path: str) -> dict:
    """get files in a directory

    Args:
        path (str): path of the directory

    Returns:
        dict: files details
    """

    files = os.listdir(path)
    details = {}
    for file in files:
        file_name = file
        file = path + "/" + file
        file_size = os.path.getsize(file)
        file_type = mimetypes.guess_type(file)
        if file_type[0] is None:
            file_type = "Folder"
        else:
            file_type = file_type[0]
        created_at = datetime.datetime.fromtimestamp(os.path.getctime(file))
        details[file_name] = {
            "file_name": file_name,
            "file_size": convert_file_size(file_size),
            "file_type": file_type,
            "created_at": datetime.datetime.strftime(created_at, "%Y-%m-%d %H:%M:%S"),
            "path": file,
        }
    # sort the files by type
    details = dict(sorted(details.items(), key=lambda item: item[1]["file_type"]))
    return details


def template(file_path: str) -> HTMLResponse:
    """generate html template

    Args:
        file_path (str): path of the directory

    Returns:
        HTMLResponse: html response
    """
    back = file_path.rsplit("/", 1)[0]
    back = f"http://{my_ip}:{my_port}{back}"
    table = ""
    details = get_files(file_path)
    for i in details:
        table += (
            f"""
            <tr>
                <td><a href="{f"http://{my_ip}:{my_port}" + details[i]['path']}">{i}</a></td>
                <td>"""
            + details[i]["file_size"]
            + """</td>
                <td>"""
            + details[i]["file_type"]
            + """</td>
                <td>"""
            + details[i]["created_at"]
            + """</td>
            </tr>
        """
        )
    html = (
        """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>File Sharing</title>
        <style>
            table {
                font-family: arial, sans-serif;
                border-collapse: collapse;
                width: 100%;
            }
            td, th {
                border: 1px solid #dddddd;
                text-align: left;
                padding: 8px;
            }
            tr:nth-child(even) {
                background-color: #dddddd;
            }
            th {
                background-color: #4CAF50;
                color: white;
            }
            tr:hover {
                background-color: #f5f5f5;
            }
            a {
                color: #4CAF50;
                text-decoration: none;
            }
        </style>
    </head>
    <body>
        <a color="green"; href="https://github.com/MohammadrezaAmani/">Github</a>
        <br>
        <a href="""
        + back
        + """>Back</a>
        <form action="/uploadfile/" enctype="multipart/form-data" method="post">
                <input name="file_path" type="hidden" value=\""""
        + file_path
        + """\">
                <input type="file" name="file">
            <input type="submit">
            
        <table>
            <tr>
                <th>File Name</th>
                <th>File Size</th>
                <th>File Type</th>
                <th>Created At</th>
            </tr>
            """
        + table
        + """
        </table>
    </body>
    """
    )
    return HTMLResponse(content=html, status_code=200)


@app.post("/uploadfile/")
async def create_upload_file(
    file_path: str = File(description="A file path"),
    file: UploadFile = File(description="A file read as UploadFile"),
):
    if file_path.startswith("//"):
        file_path = file_path[1:]
    with open(file_path + "/" + file.filename, "wb") as buffer:
        buffer.write(file.file.read())
        print(file_path + file.filename)
    url = f"http://{my_ip}:{my_port}{file_path}"
    print(url)
    return RedirectResponse(
        url=url,
        status_code=303,
    )


def download(file_path: str) -> StreamingResponse:
    """download file

    Args:
        file_path (str): path of the file

    Returns:
        StreamingResponse: file response
    """
    media_type = mimetypes.guess_type(file_path)[0]
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
        return FileResponse(file_path, media_type=media_type)


@app.get("{file_path:path}")
def read_file(file_path: str):
    if not os.path.exists(file_path):
        return {"status": "path not found"}
    if not os.path.isdir(file_path):
        return download(file_path)

    return template(file_path)


def generate_qr_code() -> None:
    """generate qr code for the given path

    Example:
        python3 main.py /home/blackBug/Downloads

    Returns:
        None: None

    Raises:
        Exception: if the path is not given
    """
    import sys

    if len(sys.argv) == 2:
        try:
            import qrcode
        except:
            print("Please install qrcode")
            return
        my_ip = (
            subprocess.check_output(["hostname", "-I"]).decode("utf-8").split(" ")[0]
        )
        my_port = 8000
        path = os.path.abspath(sys.argv[1])
        img = qrcode.make(f"http://{my_ip}:{my_port}{path}")
        img.save("qr_code.png")
        if os.name == "posix":
            os.system("xdg-open qr_code.png")
        print("QR Code Generated")


if __name__ == "__main__":
    generate_qr_code()
    print("Server Started")
    uvicorn.run(
        app,
        host=my_ip,
        port=my_port,
    )  # log_level="error")
