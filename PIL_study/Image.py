from PIL import Image
# 创建图像
# Image.new("L", (28, 28), 255).show()
# Image.new("RGB", (28, 28), (20,200,45)).show()
im = Image.open('../images/star2.jpg')
print(im.getbands())
print(im.getcolors())
print(im.getdata())
print(im.getextrema())
# print(im.getpixel(80, 80))
print(im.histogram())

im1 = Image.open('../images/star.jpg')
# im1.convert("1").show()
# im1.convert("L").show()
w, h = im.size
print(w, h)
# Image.rotate(angle, resample=0, expand=0, center=None, translate=None)
# im.rotate(-90).show()    # 将图片旋转，并用系统自带的图片工具显示图片
# im.transpose(Image.FLIP_LEFT_RIGHT).show()    # 左右调换
# im.transpose(Image.FLIP_TOP_BOTTOM).show()    # 上下颠倒

# im.resize((200, 300), Image.NEAREST).show()  # 重置大小
# NEAREST 最近滤波。从输入图像中选取最近的像素作为输出像素。它忽略了所有其他的像素。(默认)
# BILINEAR 双线性滤波。在输入图像的2x2矩阵上进行线性插值
# BICUBIC 双立方滤波。在输入图像的4x4矩阵上进行立方插值
# ANTIALIAS 平滑滤波。这是PIL 1.1.3版本中新的滤波器。对所有可以影响输出像素的输入像素进行高质量的重采样滤波，以计算输出像素值。

# im.thumbnail((w//2, h//2))    # 缩放图片
# im.show()

# 图像处理
# 1 图像通道融合，两图size和mode一致，且要求格式为RGBA,将后者合成到前者中.如果其一是透明的，才能看到结果，不然最终结果只会显示出后者
im2 = Image.open('../images/star2.jpg').convert('RGBA')
im3 = Image.open('../images/star3.jpg').convert('RGBA')
# Image.alpha_composite(im3, im2).show()

# Image.blend(im2, im3, 0.2).show()

im4 = Image.open('../images/star2.jpg').convert('L')
# Image.composite(im2, im3, im4).show()

# eval
# Image.eval(im1, lambda i: i*5).show()  # 将原图片的像素点，都乘2，返回的是一个Image对象

# crop() paste() merge()
im03 = Image.open('../images/dog.jpg')
x, y = im03.size
xLeft = x//2
boxLeft = (0, 0, xLeft, y)  # 分成两部分
boxRight = (xLeft, 0, x, y)

boxLeftNew = (0, 0, x-xLeft, y)     # 新区域
boxRightNew = (x-xLeft, 0, x, y)

partLeft = im03.crop(boxLeft).transpose(Image.FLIP_LEFT_RIGHT).transpose(Image.ROTATE_180)   # 左右调换并旋转180度
partRight = im03.crop(boxRight)

im03.paste(partRight, boxLeftNew)
im03.paste(partLeft, boxRightNew)

# im03.show()
