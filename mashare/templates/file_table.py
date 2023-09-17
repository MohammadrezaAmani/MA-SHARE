from inui.elements import *
from .base import base
from .utils import process_path, files


def file_table(path: str = None):
    return str(
        base(
            Span( 
                data=(
                    Span(
                        data=(
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
                                                id = """upload""",
                                            ),
#                                             f"""<form action="/upload{path}" method="post" enctype="multipart/form-data">
#     <input type="file" name="name" multiple="multiple"><br><br>
#     <br>
#     <input type="submit" value="Submit">
#  </form>""",
                                            Button(
                                                typee="""button""",
                                                classs="""btn btn-secondary icon-btn mr-2""",
                                                disabled="""disabled""",
                                                data=(
                                                    I(
                                                        classs="""ion ion-md-cloud-download""",
                                                    ),
                                                ),
                                                id= """file-manager-download-btn""",
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
                    # Script(
                    #     src="""https://code.jquery.com/jquery-1.10.2.min.js""",
                    # ),
                    Script(src="/assets/js/bootstrap.min.js"),
                    Script(typee="""text/javascript""", data=()),
                    # upload script for upload button, it will open multiple file upload dialog and post them to /upload/{path}
                    Script("""


                    
                           """)
                )
            ),
            path=path,
            style='/assets/css/home.css'
        )
    )
