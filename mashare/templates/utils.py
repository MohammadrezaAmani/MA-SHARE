import os
from concurrent.futures import ThreadPoolExecutor
from mimetypes import guess_type

from inui.elements import A, Button, Div, I, Input, Label, Li, Ol, Span

from mashare.utils.utils import conf


def link_maker(path, format=None):
    ip, port = conf()
    ip = f"http://{ip}:{port}/"
    if isinstance(path, str):
        path = path.split("/")
        path = [i for i in path if i not in ["", None]]
        path = ["/"] + path

    if format:
        ip = ip + format
    ip += "/"
    return ip + "/".join([i for i in path if i != "/"])


def process_path(path: str):
    path = path.split("/")
    path = [i for i in path if i not in ["", None]]
    path = ["/"] + path
    return Ol(
        classs="""breadcrumb text-big container-p-x py-3 m-0""",
        data=(
            *[
                Li(
                    classs="""breadcrumb-item""",
                    data=(
                        A(
                            href=link_maker(path[: i + 1], format="show"),
                            data=path[i],
                        ),
                    ),
                )
                for i in range(len(path[:-1]))
            ],
            Li(
                classs="""breadcrumb-item active""",
                data=(path[-1]),
            ),
        ),
    )


def create_file(path: str):
    if not os.path.exists(path):
        return []
    path = "/" + path if not path.startswith("/") else path
    icons = {
        "folder": "far fa-folder",
        "text/x-python": "fa-brands fa-python",
        "octet-stream": "fa-brands fa-js-square",
        "application/css": "fa-brands fa-css3",
        "text/markdown": "fa-brands fa-markdown",
        "r": "fa-brands fa-r-project",
        "java": "fa-brands fa-java",
        "video": "far fa-file-video",
        "music": "fas fa-music",
        "photo": "fas fa-photo-video",
        "application/pdf": "far fa-file-pdf",
        "doc": "",
        "ppt": "far fa-file-powerpoint",
        "pptx": "far fa-file-powerpoint",
        "txt": "fa fa-file-text-o",
        "application/zip": "fa fa-file-zip-o",
        "application/7z": "fa fa-file-zip-o",
        "application/rar": "fa fa-file-zip-o",
        "html": "fa-brands fa-html5",
        "application/octet-stream": "far fa-file",
        "gitignore": "fa fa-file-text-o",
        "js": "fa-brands fa-square-js",
    }
    link_type = None
    content_type = str(guess_type(path)[0])
    file_format = path.rsplit(".")[0]
    if os.path.isdir(path):
        icon = icons["folder"]
        link_type = "show"
    elif content_type.startswith("image"):
        icon = icons["photo"]
        link_type = "photo"
    elif content_type.startswith("audio"):
        icon = icons["music"]
        link_type = "audio"
    elif content_type.startswith("video"):
        icon = icons["video"]
        link_type = "video"
    elif file_format == "ms":
        icon = icons["text/markdown"]
        link_type = "text"
    elif file_format == "js":
        icon = icons["js"]
        link_type = "text"
    elif file_format == "java":
        icon = icons["java"]
        link_type = "text"
    elif content_type.endswith("python"):
        icon = icons["text/x-python"]
        link_type = "text"
    elif content_type.startswith("text"):
        icon = icons["txt"]
        link_type = "text"
    else:
        icon = icons["application/octet-stream"]
        link_type = "dl"
    return str(
        Div(
            classs="""file-item""",
            data=(
                Div(
                    classs="""file-item-select-bg bg-primary""",
                ),
                Label(
                    classs="""file-item-checkbox custom-control custom-checkbox""",
                    data=(
                        Input(
                            typee="""checkbox""",
                            classs="""custom-control-input""",
                        ),
                        Span(
                            classs="""custom-control-label""",
                        ),
                    ),
                ),
                Div(
                    classs=f"""file-item-icon {icon} text-secondary""",
                ),
                A(
                    href=f"""{link_maker(path, link_type)}""",
                    classs="""file-item-name""",
                    data=(path.split("/")[-1]),
                ),
                Div(
                    classs="""file-item-changed""",
                    data=("""02/14/2018""",),
                ),
                Div(
                    classs="""file-item-actions btn-group""",
                    data=(
                        Button(
                            typee="""button""",
                            classs="""btn btn-default btn-sm rounded-pill icon-btn borderless md-btn-flat hide-arrow dropdown-toggle""",
                            data_toggle="""dropdown""",
                            data=(
                                I(
                                    classs="""ion ion-ios-more""",
                                ),
                            ),
                        ),
                        Div(
                            classs="""dropdown-menu dropdown-menu-right""",
                            data=(
                                A(
                                    classs="""dropdown-item""",
                                    href="""javascript:void(0)""",
                                    data=("""Rename""",),
                                ),
                                A(
                                    classs="""dropdown-item""",
                                    href="""javascript:void(0)""",
                                    data=("""Move""",),
                                ),
                                A(
                                    classs="""dropdown-item""",
                                    href="""javascript:void(0)""",
                                    data=("""Copy""",),
                                ),
                                A(
                                    classs="""dropdown-item""",
                                    href="""javascript:void(0)""",
                                    data=("""Remove""",),
                                ),
                            ),
                        ),
                    ),
                ),
            ),
        )
    )


def create_file_threaded(path, out):
    file_data = create_file(path)
    out.append(file_data)


def files(path: str):
    path = "/" + path if path.startswith("/") else path
    path = path[:-1] if path.endswith("/") else path
    if not os.path.exists(path):
        return []
    if not os.path.isdir(path):
        return []
    listdir = os.listdir(path)
    out = []

    with ThreadPoolExecutor(max_workers=30) as executor:
        futures = []
        for i in listdir:
            file_path = path + "/" + i
            future = executor.submit(create_file_threaded, file_path, out)
            futures.append(future)

        for future in futures:
            future.result()

    return out
