"base"
from inui.elements import Html, Body, Link, Div, Script, Hr
from .header import header
from .utils import process_path


def base(body, path=None, style=None, script=None):
    "base style"
    return str(
        Html(
            lang="""en""",
            data=(
                header(style),
                str(
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
                                        ),
                                    ),
                                ),
                            ),
                            body,
                            Script(
                                src="""https://code.jquery.com/jquery-1.10.2.min.js""",
                            ),
                            Script(src="/assets/js/bootstrap.min.js"),
                            Script(typee="""text/javascript""", data=()),
                        )
                    )
                ),
            ),
        )
    )
