#第 0010 题：使用 Python 生成字母验证码图片
import random
import string
from PIL import Image,ImageDraw,ImageFont,ImageFilter
def Get_Random_Char():
    return[random.choice(string.ascii_letters) for _ in range(4)]#返回一个list
def Get_Random_Color():
    return(random.randint(30,100),random.randint(30,100),random.randint(30,100))#颜色由三个值构成，是一个tuple？
def Get_Validate_Image():
    NewImg = Image.new("RGBA", (240, 60), (180, 180, 180))
    #NewImg.save("newImg.png", "PNG")
    Random_Char = Get_Random_Char()
    fnt = ImageFont.truetype('C:/Windows/Fonts/STZHONGS.TTF', 40)
    draw = ImageDraw.Draw(NewImg)
    for i in range(4):
        draw.text((60*i+20, 3+random.randint(-15,15)), Random_Char[i], fill=Get_Random_Color(), font=fnt)
    for _ in range(random.randint(1000, 2000)):
        draw.point((random.randint(0, 240), random.randint(0, 60)), fill=Get_Random_Color())#添加噪点
    NewImg = NewImg.filter(ImageFilter.BLUR)#模糊
    del draw
    NewImg.show()
    #print(Random_Color)
if __name__ == '__main__':
    Get_Validate_Image()