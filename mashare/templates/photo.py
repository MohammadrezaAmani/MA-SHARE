from inui.elements import Img
from .base import base
from .utils import link_maker


def photo(path: str):
    return str(
        base(
            str(
                Img(
                    src=link_maker(path, "dl"),
                )
            ),
            path=path,
            style='/assets/css/photo.css'
        )
    )
