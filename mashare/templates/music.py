from inui.elements import *

from .base import base
from .utils import link_maker, process_path


def music(path: str):
    return str(
        base(
            """<div class="music-player">
        <audio id="audio" src="%s" controls></audio>
        <div class="controls">
            <button id="play-pause">Play</button>
            <button id="stop">Stop</button>
        </div>
    </div>
    <script src="/assets/js/music.js"></script>"""
            % link_maker(path=path, format="dl"),
            path=path,
        ),
    )
