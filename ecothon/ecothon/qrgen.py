import qrcode
import sys
import time
from PIL import Image

qr = qrcode.QRCode(
    version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=50, border=2)

qr.add_data(
    "Congratulations, you got 10 percent discount coupon on iamgardener! Your Promo Code is wercjj23")

qr.make(fit=True)
img = qr.make_image(fill_color='green', back_color='white')
logo_display = Image.open('ecodesleaf.png')
logo_display.thumbnail((400, 400))

logo_pos = ((img.size[0] - logo_display.size[0]) // 2,
            (img.size[1] - logo_display.size[1]) // 2)
img.paste(logo_display, logo_pos)

img.save('ecodes1.png')
qr = qrcode.QRCode(
    version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=50, border=2)

qr.add_data("Congratulations, you got 15 percent discount coupon on Chay ya! Your Promo Code is pocjj23")

qr.make(fit=True)
img = qr.make_image(fill_color='green', back_color='white')
logo_display = Image.open('ecodesleaf.png')
logo_display.thumbnail((400, 400))

logo_pos = ((img.size[0] - logo_display.size[0]) // 2,
            (img.size[1] - logo_display.size[1]) // 2)
img.paste(logo_display, logo_pos)

img.save('ecodes2.png')
qr = qrcode.QRCode(
    version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=50, border=2)

qr.add_data(
    "Congratulations, you got 20 percent discount coupon on Chay ya! Your Promo Code is zxrjj23")

qr.make(fit=True)
img = qr.make_image(fill_color='green', back_color='white')
logo_display = Image.open('ecodesleaf.png')
logo_display.thumbnail((400, 400))

logo_pos = ((img.size[0] - logo_display.size[0]) // 2,
            (img.size[1] - logo_display.size[1]) // 2)
img.paste(logo_display, logo_pos)

img.save('ecodes3.png')
qr = qrcode.QRCode(
    version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=50, border=2)

qr.add_data(
    "Congratulations, you got 100 points.")

qr.make(fit=True)
img = qr.make_image(fill_color='green', back_color='white')
logo_display = Image.open('ecodesleaf.png')
logo_display.thumbnail((400, 400))

logo_pos = ((img.size[0] - logo_display.size[0]) // 2,
            (img.size[1] - logo_display.size[1]) // 2)
img.paste(logo_display, logo_pos)
img.save('ecodes4.png')
qr = qrcode.QRCode(
    version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=50, border=2)

qr.add_data(
    "You have just scanned the qr near dustbin, and you earned 50 points!")

qr.make(fit=True)
img = qr.make_image(fill_color='green', back_color='white')
logo_display = Image.open('ecodesleaf.png')
logo_display.thumbnail((400, 400))

logo_pos = ((img.size[0] - logo_display.size[0]) // 2,
            (img.size[1] - logo_display.size[1]) // 2)
img.paste(logo_display, logo_pos)
img.save('ecodes5.png')
