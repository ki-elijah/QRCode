import pyqrcode
import png
from pyqrcode import QRCode
import os.path

save_path = 'Pictures'

e = input("Enter the amount of money or number for the item: ")
url = pyqrcode.create(e)
url.svg("code.svg", scale = 10)
url.png('code.png', scale = 10)
