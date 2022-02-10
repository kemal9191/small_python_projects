import qrcode
from pyzbar.pyzbar import decode
from PIL import Image
import sys

'''
This small program begins with asking you necessary information to create a QR code.
After creating a QR code, it moves on with asking you whether you would like to read
a QR code. If yes, program reads the QR code that is located on path you provide, 
otherwise, program is terminated. 
'''

data = input('Please enter a string:\n>')

if data == '':
    data = input('Please enter a valid string:\n>')
else:
    file_name = input('Please enter your file name:\n>') + '.png'
    
    if file_name =='':
        file_name = input('Please enter a valid file name:\n>') + '.png'
    else:
        location = input('Please specify where to save the QR code:\n>')+'/'+file_name        
        try:
            img = qrcode.make(data)
            img.save(location)
            print('Your QR code has been generated!')
        except Exception:
            print(sys.exc_info())
    

decoding_image = input('If you proceed by decoding an image, please enter its location:\n>')

if decoding_image == '':
    print('Program terminated')
else:
    try:
        img = Image.open(decoding_image)
        result = decode(img)
        print(result)
    except:
        print(sys.exc_info())




