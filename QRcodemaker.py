import qrcode as qr



def qrcode_Gen(url):
    #url='http://arunprasath08.pythonanywhere.com/'
    qrcd=qr.make(url)
    qrcd.save(r'C:\Users\Arun\pythoncode\websiteimg.png')

link=input('Enter something that need to be QR coded')

if __name__=="__main__":
    qrcode_Gen(link)
