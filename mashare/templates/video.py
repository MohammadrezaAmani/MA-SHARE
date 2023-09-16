from inui.elements import Div, Video, Button, I, Script
from .base import base


def video_player(path):
    return str(
        base(
            str(
                Div(
                    classs="""container""",
                    data=(
                        Video(
                            onclick="""play(event)""",
                            src="/dl" + path,
                            id="""video""",
                        ),
                        Div(
                            classs="""controls""",
                            data=(
                                Button(
                                    onclick="""play(event)""",
                                    data=(
                                        I(
                                            classs="""fa fa-play""",
                                        ),
                                        I(
                                            classs="""fa fa-pause""",
                                        ),
                                    ),
                                ),
                                Button(
                                    onclick="""rewind(event)""",
                                    data=(
                                        I(
                                            classs="""fa fa-fast-backward""",
                                        ),
                                    ),
                                ),
                                Div(
                                    classs="""timeline""",
                                    data=(
                                        Div(
                                            classs="""bar""",
                                            data=(
                                                Div(
                                                    classs="""inner""",
                                                ),
                                            ),
                                        ),
                                    ),
                                ),
                                Button(
                                    onclick="""forward(event)""",
                                    data=(
                                        I(
                                            classs="""fa fa-fast-forward""",
                                        ),
                                    ),
                                ),
                                Button(
                                    onclick="""fullScreen(event)""",
                                    data=(
                                        I(
                                            classs="""fa fa-expand""",
                                        ),
                                    ),
                                ),
                                Button(
                                    onclick="""download(event)""",
                                    data=(
                                        I(
                                            classs="""fa fa-cloud-download""",
                                        ),
                                    ),
                                ),
                            ),
                        ),
                        Script(
                            src="""/assets/js/video.min.js""",
                        ),
                    ),
                ),
            ),
            style="""/assets/css/video.min.css""",
            path=path,
        )
    )
