import qrcode

image = qrcode.make("https://1270.0.0.1:8000")
image.save("qr.png")