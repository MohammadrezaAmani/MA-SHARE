# -------------- Imports --------------
import os
import sys
import subprocess

# -------------- QR code --------------


def generate_qr_code() -> None:
    """generate qr code for the given path

    Example:
        python3 main.py /home/blackBug/Downloads

    Returns:
        None: None

    Raises:
        Exception: if the path is not given
    """
    import sys

    if len(sys.argv) == 2:
        try:
            import qrcode
        except:
            print("Please install qrcode")
            return
        IP = subprocess.check_output(["hostname", "-I"]).decode("utf-8").split(" ")[0]
        PORT = 8000
        path = os.path.abspath(sys.argv[1])
        img = qrcode.make(f"http://{IP}:{PORT}{path}")
        img.save("qr_code.png")
        if os.name == "posix":
            os.system("xdg-open qr_code.png")
        print("QR Code Generated")
