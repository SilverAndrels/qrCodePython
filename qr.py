import qrcode
print("Hi, this is the QRcode generator using python!")
link = input('Paste the link: ')
image_qr = qrcode.make(link)
name = input("QR name and extension:(example: name.png...) ")
image_qr.save(name)
