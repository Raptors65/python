import qrcode

qr = qrcode.QRCode(
	version=None,
	box_size=10
)
qr.add_data("Test")
qr.make(fit=True)

img = qr.make_image()
img.show()
