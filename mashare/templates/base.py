"base"
import os
from mimetypes import guess_type
from inui.elements import *
from mashare.utils.utils import conf
from .header import header
from .footer import footer


def link_maker(path, format="show"):
    ip, port = conf()
    ip = f"http://{ip}:{port}/"
    if type(path) == str:
        path = path.split("/")
        path = [i for i in path if i not in ["", None]]
        path = ["/"] + path

    if format:
        ip = ip + format
    ip += "/"
    return ip + "/".join([i for i in path if i != "/"])


def process_path(path):
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
                            href=link_maker(path[: i + 1]),
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
        "text/x-python": "fab fa-python",
        "octet-stream": "fab fa-js-square",
        "application/css": "fab fa-css3",
        "text/markdown": "ab fa-markdown",
        "r": "fab fa-r-project",
        "text/java": "fab fa-java",
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
        "html": "far fa-file-code",
        "application/octet-stream": "far fa-file",
        "gitignore": "fa fa-file-text-o",
    }
    l = None
    content_type = str(guess_type(path)[0])
    file_format = path.rsplit(".")[0]
    if os.path.isdir(path):
        icon = icons["folder"]
        l = "show"
    elif content_type.startswith("image"):
        icon = icons["photo"]
        l = "photo"
    elif content_type.startswith("audio"):
        icon = icons["music"]
        l = "audio"
    elif content_type.startswith("video"):
        icon = icons["video"]
        l = "video"
    elif content_type.startswith("text"):
        icon = icons["txt"]
        l = "text"
    else:
        icon = icons["application/octet-stream"]
        l = "dl"
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
                    href=f"""{link_maker(path, l)}""",
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


def files(path: str):
    path = "/" + path if path.startswith("/") else path
    path = path[:-1] if path.endswith("/") else path
    if not os.path.exists(path):
        return []
    if not os.path.isdir(path):
        return []
    listdir = os.listdir(path)
    out = []
    for i in listdir:
        out.append(create_file(path + "/" + i))
    return out


def base(path: str = None):
    "base style"
    return str(
        Html(
            lang="""en""",
            data=(
                header(),
                Body(
                    data=(
                        Link(
                            rel="""stylesheet""",
                            href="""https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.13.1/css/all.min.css""",
                            integrity="""sha256-2XFplPlrFClt0bIdPgpz8H7ojnk10H69xRqd9+uTShA=""",
                            crossorigin="""anonymous""",
                        ),
                        Link(
                            rel="""stylesheet""",
                            href="""https://cdnjs.cloudflare.com/ajax/libs/ionicons/4.5.6/css/ionicons.min.css""",
                            integrity="""sha512-0/rEDduZGrqo4riUlwqyuHDQzp2D1ZCgH/gFIfjMIL5az8so6ZiXyhf1Rg8i6xsjv+z/Ubc4tt1thLigEcu6Ug==""",
                            crossorigin="""anonymous""",
                            referrerpolicy="""no-referrer""",
                        ),
                        Div(
                            classs="""container flex-grow-1 light-style container-p-y""",
                            data=(
                                Div(
                                    classs="""container-m-nx container-m-ny bg-lightest mb-3""",
                                    data=(
                                        process_path(path),
                                        Hr(
                                            classs="""m-0""",
                                        ),
                                        Div(
                                            classs="""file-manager-actions container-p-x py-2""",
                                            data=(
                                                Div(
                                                    data=(
                                                        Button(
                                                            typee="""button""",
                                                            classs="""btn btn-primary mr-2""",
                                                            data=(
                                                                I(
                                                                    classs="""ion ion-md-cloud-upload""",
                                                                ),
                                                            ),
                                                        ),
                                                        Button(
                                                            typee="""button""",
                                                            classs="""btn btn-secondary icon-btn mr-2""",
                                                            disabled="""disabled""",
                                                            data=(
                                                                I(
                                                                    classs="""ion ion-md-cloud-download""",
                                                                ),
                                                            ),
                                                        ),
                                                        Div(
                                                            classs="""btn-group mr-2""",
                                                            data=(
                                                                Button(
                                                                    typee="""button""",
                                                                    classs="""btn btn-default md-btn-flat dropdown-toggle px-2""",
                                                                    data_toggle="""dropdown""",
                                                                    data=(
                                                                        I(
                                                                            classs="""ion ion-ios-settings""",
                                                                        ),
                                                                    ),
                                                                ),
                                                                Div(
                                                                    classs="""dropdown-menu""",
                                                                    data=(
                                                                        A(
                                                                            classs="""dropdown-item""",
                                                                            href="""javascript:void(0)""",
                                                                            data=(
                                                                                """Move""",
                                                                            ),
                                                                        ),
                                                                        A(
                                                                            classs="""dropdown-item""",
                                                                            href="""javascript:void(0)""",
                                                                            data=(
                                                                                """Copy""",
                                                                            ),
                                                                        ),
                                                                        A(
                                                                            classs="""dropdown-item""",
                                                                            href="""javascript:void(0)""",
                                                                            data=(
                                                                                """Remove""",
                                                                            ),
                                                                        ),
                                                                    ),
                                                                ),
                                                            ),
                                                        ),
                                                    )
                                                ),
                                                Div(
                                                    data=(
                                                        Div(
                                                            classs="""btn-group btn-group-toggle""",
                                                            data_toggle="""buttons""",
                                                            data=(
                                                                Label(
                                                                    classs="""btn btn-default icon-btn md-btn-flat active""",
                                                                    data=(
                                                                        Input(
                                                                            typee="""radio""",
                                                                            name="""file-manager-view""",
                                                                            value="""file-manager-col-view""",
                                                                            checked="""checked""",
                                                                        ),
                                                                        Span(
                                                                            classs="""ion ion-md-apps""",
                                                                        ),
                                                                    ),
                                                                ),
                                                                Label(
                                                                    classs="""btn btn-default icon-btn md-btn-flat""",
                                                                    data=(
                                                                        Input(
                                                                            typee="""radio""",
                                                                            name="""file-manager-view""",
                                                                            value="""file-manager-row-view""",
                                                                        ),
                                                                        Span(
                                                                            classs="""ion ion-md-menu""",
                                                                        ),
                                                                    ),
                                                                ),
                                                            ),
                                                        ),
                                                    )
                                                ),
                                            ),
                                        ),
                                        Hr(
                                            classs="""m-0""",
                                        ),
                                    ),
                                ),
                                Div(
                                    classs="""file-manager-container file-manager-col-view""",
                                    data=(
                                        Div(
                                            classs="""file-manager-row-header""",
                                            data=(
                                                Div(
                                                    classs="""file-item-name pb-2""",
                                                    data=("""Filename""",),
                                                ),
                                                Div(
                                                    classs="""file-item-changed pb-2""",
                                                    data=("""Changed""",),
                                                ),
                                            ),
                                        ),
                                        *files(path),
                                    ),
                                ),
                            ),
                        ),
                        Script(
                            src="""https://code.jquery.com/jquery-1.10.2.min.js""",
                        ),
                        Script(src="./assets/js/bootstrap.min.js"),
                        Script(typee="""text/javascript""", data=()),
                    )
                ),
            ),
        )
    )
