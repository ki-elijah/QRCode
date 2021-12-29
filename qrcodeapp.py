import pyqrcode
import png
from pyqrcode import QRCode

e = "nze_kizito"
url = pyqrcode.create(e)
url.svg("code.svg", scale = 8)
url.png('code.png', scale = 6)