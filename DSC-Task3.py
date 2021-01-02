import qrcode
import os
from pyzbar.pyzbar import decode
from PIL import Image

print('PROGRAM TO GENERATE AND DECODE A QR CODE')
print('Enter 1 to Generate a QR code')
print('Enter 2 to Decode a QR code')
a = input()
if a=='1':
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    print('Enter data to encode')
    qr.add_data(input())
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(os.getcwd()+'/qrcode.jpg')
    print('QR Code is saved in current directory as "qrcode.jpg"')
elif a =='2':
    print("Enter the QR Code's file name. (Save it in current directory)")
    img = Image.open(input())
    result = decode(img)[0].data.decode("utf-8")
    print("Decoded result =",result)
