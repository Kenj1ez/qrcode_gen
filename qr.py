# qrcode gen

import qrcode

link = input("Enter your link for which you need QR code: ")
name = input("Enter the file name: ")

try:
  img = qrcode.make(link)
  img.save(name , format="png")
  print("Your QR code has been generated")
  except:
  print("Please Enter a valid URL")

