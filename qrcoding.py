import qrcode

x=input("Enter the text or URL: ")
y=input("Enter the file name")

qr=qrcode.make(x)
qr.save(y)