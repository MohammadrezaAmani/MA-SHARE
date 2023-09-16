// script.js
const audio = document.getElementById("audio");
const playPauseButton = document.getElementById("play-pause");
const stopButton = document.getElementById("stop");

playPauseButton.addEventListener("click", togglePlayPause);
stopButton.addEventListener("click", stopAudio);

function togglePlayPause() {
    if (audio.paused || audio.ended) {
        audio.play();
        playPauseButton.textContent = "Pause";
    } else {
        audio.pause();
        playPauseButton.textContent = "Play";
    }
}

function stopAudio() {
    audio.pause();
    audio.currentTime = 0;
    playPauseButton.textContent = "Play";
}
