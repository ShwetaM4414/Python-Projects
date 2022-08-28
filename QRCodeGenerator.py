import pyqrcode

str = input("Enter url or any text : ")
code = pyqrcode.create(str)
code.svg("qrcode.svg")
code.png('qrcode.png')
