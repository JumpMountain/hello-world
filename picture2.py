import base64
import io
import PIL.Image as Image
# 图片转换成base64
def picture2base(path):
    with open(path, 'rb') as img_file:
        img_b64encode = base64.b64encode(img_file.read())
        s = img_b64encode.decode()
        resbase64='data:image/jpeg;base64,%s' % s
        return resbase64

# base64转换成图片
def base2picture(resbase64):
    res=resbase64.split(',')[1]
    img_b64decode = base64.b64decode(res)
    image = io.BytesIO(img_b64decode)
    print(image)
    img = Image.open(image)
    img.show()


t=picture2base('1.jpg')
print(t)
base2picture(t)
