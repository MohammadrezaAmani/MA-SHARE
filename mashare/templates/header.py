from inui.elements import *
from mashare import BASE_PATH


def header(style=None, script=None):
    return str(
        Head(
            data=(
                Meta(
                    charset="""utf-8""",
                ),
                Title(data=("""check file manager - Bootdey.com""",)),
                Meta(
                    name="""viewport""",
                    content="""width=device-width, initial-scale=1""",
                ),
                Link(
                    rel="""stylesheet""",
                    href="""https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css""",
                    integrity="""sha512-Fo3rlrZj/k7ujTnHg4CGR2D7kSs0v4LLanw2qksYuRlEzO+tcaEPQogQ0KaoGN26/zrn20ImR1DfuLWnOo7aBA==""",
                    crossorigin="""anonymous""",
                    referrerpolicy="""no-referrer""",
                ),
                Link(
                    href="""/assets/css/bootstrap.min.css""",
                    rel="""stylesheet""",
                ),
                Link(
                    href="""/assets/css/home.css""",
                    rel="""stylesheet""",
                ),
                Link(
                    href=style,
                    rel="""stylesheet""",
                )
                if style is not None
                else "",
            )
        )
    )
