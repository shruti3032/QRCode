import qrcode
from PIL import Image

qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size=10,
                   border=2,
                   ) # To change color,border and other specilities of qrcode
qr.add_data("https://www.hackerrank.com/shrutikamble3032")
qr.make(fit=True)
img = qr.make_image(fill_color="#FBEEE6",back_color="#A04000")
img.save("hackerrank.png")