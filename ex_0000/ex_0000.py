from PIL import Image,ImageDraw,ImageFont
filepath = "img/touxiang.jpg"
outpath = "img/touxiang2.jpg"
try:
    pic = Image.open(filepath)
except IOError:
    print("cannot open",filepath)
fnt = ImageFont.truetype('C:/Windows/Fonts/STZHONGS.TTF', 40)
draw = ImageDraw.Draw(pic)
draw.text((200,5),'4',fill="#ff0000",font=fnt)
del draw
pic.show()
pic.save(outpath)