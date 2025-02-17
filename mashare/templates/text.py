from inui.elements import Button, Div, Script, Textarea

from .base import base


def text_editor(path, text=None):
    return str(
        base(
            str(
                Div(
                    classs="container",
                    id="screen",
                    data=(
                        Div(
                            classs="""editor-container""",
                            data=(
                                Div(
                                    classs="""editor""",
                                    data=(
                                        Textarea(
                                            id="""text-area""",
                                            data=text,
                                            placeholder="""Type your text here...""",
                                        ),
                                        Div(
                                            classs="""controls""",
                                            data=(
                                                Button(
                                                    id="""save-button""",
                                                    data=("""Save""",),
                                                ),
                                                Button(
                                                    id="""load-button""",
                                                    data=("""Load""",),
                                                ),
                                            ),
                                        ),
                                    ),
                                ),
                            ),
                        ),
                        Script(
                            src="""/assets/js/text.js""",
                        ),
                    ),
                )
            ),
            path=path,
            style="/assets/css/text.css",
        )
    )
