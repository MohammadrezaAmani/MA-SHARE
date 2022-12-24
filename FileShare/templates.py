# get IP address
from FileShare import get_files
from fastapi.responses import HTMLResponse
from FileShare import IP, PORT

# ------------- Templates -------------
def template(file_path: str, sorting: int = 0) -> HTMLResponse:
    """generate html template

    Args:
        file_path (str): path of the directory

    Returns:
        HTMLResponse: html response
    """
    back = file_path.rsplit("/", 1)[0]
    back = f"http://{IP}:{PORT}{back}"
    table = ""
    details = get_files(file_path)

    # TODO: complete sort options
    if sorting == 0:
        details = dict(sorted(details.items(), key=lambda item: item[0]))
    if sorting == 1:
        details = dict(sorted(details.items(), key=lambda item: item[1]["file_size"]))
    if sorting == 2:
        details = dict(sorted(details.items(), key=lambda item: item[1]["file_type"]))
    if sorting == 3:
        details = dict(sorted(details.items(), key=lambda item: item[1]["created_at"]))
    if sorting == 4:
        details = dict(sorted(details.items(), key=lambda item: item[0], reverse=True))
    if sorting == 5:
        details = dict(
            sorted(details.items(), key=lambda item: item[1]["file_size"], reverse=True)
        )
    if sorting == 6:
        details = dict(
            sorted(details.items(), key=lambda item: item[1]["file_type"], reverse=True)
        )
    if sorting == 7:
        details = dict(
            sorted(
                details.items(), key=lambda item: item[1]["created_at"], reverse=True
            )
        )

    for i in details:
        if not details[i]["file_type"] == "Folder":
            path = f"http://{IP}:{PORT}/dl" + details[i]["path"]
            table += (
                f"""
                <tr>
                    <td><a href="{path}">{i}</a></td>
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

        else:

            path = f"http://{IP}:{PORT}" + details[i]["path"]
            table += (
                f"""
                <tr>
                    <td><a href="{path}">{i}</a></td>
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


def textEditore_template(file_path: str) -> HTMLResponse:
    """generate html template for text editor

    Args:
        file_path (str): path of the file

    Returns:
        HTMLResponse: html response
    """

    with open(file_path, "r") as f:
        file_content = f.read()
    # some characters are not allowed in html
    bads = ["<", ">", '"', "'"]
    if any(bad in file_content for bad in bads):
        file_content = file_content.replace("<", "&lt;")
        file_content = file_content.replace(">", "&gt;")
        file_content = file_content.replace('"', "&quot;")
        file_content = file_content.replace("'", "&apos;")
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
            textarea {
                width: 100%;
                height: 100%;
                background-color: black;
                color: green;
            }
            body {
                margin: 0;
                padding: 0;
            }
            input {
                width: 100%;
                height: 50px;
                font-size: 20px;
                color: red;
                background-color: black;
            }
            html {
                background-color: black;
            }
        </style>
    </head>
    <body>
        <form action = "/textEditor/" method = "post">
            <input name="file_path" type="hidden" value=\""""
        + file_path
        + """\">
            <textarea name="file_content" rows="50" cols="500">"""
        + file_content
        + """</textarea>
            <input type="submit">
        </form>
    </body>
    """
    )
    return HTMLResponse(content=html, status_code=200)


def musicPlayer(file_path: str) -> HTMLResponse:
    """generate html template for music player

    Args:
        file_path (str): path of the file

    Returns:
        HTMLResponse: html response
    """
    html = (
        """
    <!DOCTYPE html> 
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>File Sharing</title>
    </head>
    <body>
        <audio controls>
            <source src=\""""
        + file_path
        + """\" type="audio/mpeg">
        </audio>
    </body>
    """
    )
    return HTMLResponse(content=html, status_code=200)


def videoPlayer(file_path: str) -> HTMLResponse:
    """generate html template for video player

    Args:
        file_path (str): path of the file

    Returns:
        HTMLResponse: html response
    """
    html = (
        """ 
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>File Sharing</title>
    </head> 
    <body>
        <video width="100%" height="100%" controls> <source src=\""""
        + file_path
        + """\" type="video/mp4">
        </video>
    </body>
    """
    )
    return HTMLResponse(content=html, status_code=200)
