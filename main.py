"""FastAPI File Sharing By Mohammadreza Amani"""
# ------------- Imports -------------
import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
# from mashare.routes.download import router as downloadrouter
# from mashare.routes.edit import router as editrouter
# from mashare.routes.mainrouter import router as mainrouter
# from mashare.routes.upload import router as uploadrouter
from mashare.utils.utils import conf
from mashare.utils.qr import generate_qr_code
from mashare.templates.base import base

if __name__ == "__main__":
    app = FastAPI()
    # app.include_router(mainrouter)
    # app.include_router(downloadrouter)
    # app.include_router(uploadrouter)
    # app.include_router(editrouter)
    app.mount("/assets", StaticFiles(directory="assets"), name="assets")
    @app.get("/")
    async def redirect():
        "show root files"
        return HTMLResponse(base())

    IP, PORT = conf()
    generate_qr_code(IP, PORT)
    print(f"Server is running on http://{IP}:{PORT}")
    print("Server Started")
    uvicorn.run(app, host=IP, port=PORT, log_level="error")
