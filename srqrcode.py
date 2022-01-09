import qrcode
img = qrcode.make("http://www.yukselirmi.com/")
img.save("yukselirmi.jpg")
