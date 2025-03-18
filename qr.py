# qrcode gen

import qrcode

link = input("Enter your link for which you need QR code: ")
name = input("Enter the file name: ")
img = qrcode.make (link)
type(img)
img.save(name, format="png")
