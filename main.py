import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles

from mashare.routes.download import router as downloadrouter
from mashare.routes.edit import router as editrouter
from mashare.routes.mainrouter import router as mainrouter
from mashare.routes.music import router as musicrouter
from mashare.routes.photo import router as photorouter
from mashare.routes.upload import router as uploadrouter
from mashare.routes.video import router as videorouter
from mashare.utils.qr import generate_qr_code
from mashare.utils.utils import conf

app = FastAPI()
app.mount("/assets", StaticFiles(directory="assets"), name="assets")
app.include_router(downloadrouter)
app.include_router(videorouter)
app.include_router(musicrouter)
app.include_router(photorouter)
app.include_router(uploadrouter)
app.include_router(editrouter)
app.include_router(mainrouter)


@app.get("/")
async def redirect():
    "show root files"
    return RedirectResponse("/show/")


if __name__ == "__main__":
    IP, PORT = conf()
    generate_qr_code(IP, PORT)
    print(f"Server is running on http://{IP}:{PORT}")
    print("Server Started")
    uvicorn.run(app, host=IP, port=PORT)
