import qrcode
from io import BytesIO
#import tkinter
from PIL import Image

qr = qrcode.QRCode(version=1)
text = '''
It’s safe to say my faith in American politics vanished after Hillary Clinton lost the 2016 presidential election. Like many, I had invested my heart and soul in her campaign—and, even more, in the idea of a woman finally leading our country.
For weeks the pain I felt after her loss was unbearable. I couldn’t believe I had to endure a man like Donald Trump as president for the next four years. I decided I was naive to think that America had parted ways with its history of unbridled oppression. In short, I was jaded.
I lost my enthusiasm for political affairs and instead took on the belief that the government — and sometimes the world — was ultimately against me. Afraid of being disappointed by caring too much, I decided maybe it was best not to care at all.
The election had the exact opposite effect on my mother, a lawyer for more than 20 years. Instead of feeling defeated by the results, she was inspired.
'''
qr.add_data(text)
qr.make(fit=True)
x = qr.make_image()
b = BytesIO()
x.save(b, 'PNG')
pil_image = Image.open(b)
pil_image.show()
b.close()
