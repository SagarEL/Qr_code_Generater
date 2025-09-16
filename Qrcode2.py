import qrcode as qrcode
from PIL import Image

qr = qrcode.QRCode(version = 5, 
                box_size = 40,
                border = 4,)

qr.add_data("https://www.youtube.com/watch?v=FOGRHBp6lvM&list=PLjVLYmrlmjGfAUdLiF2bQ-0l8SwNZ1sBl")
qr.make(fit = True)
img = qr.make_image(fill_color = "red", back_color = "white")
img.save("Second.png")