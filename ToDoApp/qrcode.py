import qrcode
img = qrcode.make('https://yahoo.com')
img.save('Yahoo!.png')
img.show() 