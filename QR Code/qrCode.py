import qrcode as qr

img = qr.make("https://www.youtube.com/watch?v=FOGRHBp6lvM&list=LL&index=2&t=162s")
img.save("wscube-youtube.png")

