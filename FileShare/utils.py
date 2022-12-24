# -------------- Imports --------------
import os
import mimetypes
import datetime

# ------------- Functions -------------
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

    details = dict(sorted(details.items(), key=lambda item: item[1]["file_type"]))
    return details


import subprocess

# get IP address
IP = subprocess.check_output(["hostname", "-I"]).decode("utf-8").split(" ")[0]
PORT = 8000
