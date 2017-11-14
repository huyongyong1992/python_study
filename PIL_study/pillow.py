# 利用Pillow进行图片处理
from PIL import Image, ImageFilter, ImageDraw, ImageFont, ImageChops

im= Image.open('../images/dog.jpg')
w, h = im.size
print(im.filename, im.format, im.width, im.height, im.size, im.mode, im.palette, im.info)
# If mode is “P”, palette should be an instance of the ImagePalette class. Otherwise, it should be set to None


# Image 模块
print(im.split())
print(im.getchannel('R'))
print(im.tell())

# FLIP_LEFT_RIGHT FLIP_TOP_BOTTOM ROTATE_90 ROTATE_180 ROTATE_270 TRANSPOSE TRANSVERSE

# 2.ImageFilter模块

image = Image.open('../images/dog.jpg')    #模糊图片
im2 = image.filter(ImageFilter.BLUR)
im2.save('../pillowImages/blur_dog.jpg', 'jpeg')

im3 = image.filter(ImageFilter.DETAIL)  #图片增强滤镜
im3.save('../pillowImages/detail_dog.jpg', 'jpeg')

im4 = image.filter(ImageFilter.EDGE_ENHANCE)    #图像边缘增强
im4.save('../pillowImages/edge_dog.jpg', 'jpeg')

im5 = image.filter(ImageFilter.SMOOTH)          #平滑
im5.save('../pillowImages/smooth_dog.jpg', 'jpeg')

im6 = image.filter(ImageFilter.SHARPEN)
im6.save('../pillowImages/sharpen_dog.jpg', 'jpeg')    # 锐化

im7 = image.filter(ImageFilter.EMBOSS)
im7.save('../pillowImages/emboss_dog.jpg', 'jpeg')    # 浮雕

im8 = image.filter(ImageFilter.CONTOUR)             #轮廓
im8.save('../pillowImages/contour_dog.jpg', 'jpeg')

im9 = image.filter(ImageFilter.FIND_EDGES)             #
im9.save('../pillowImages/find_edge_dog.jpg', 'jpeg')

im10 = image.filter(ImageFilter.EDGE_ENHANCE_MORE)             #
im10.save('../pillowImages/edge_more_dog.jpg', 'jpeg')

# 3.ImageDraw模块
imd = Image.open('../images/star.jpg')
draw = ImageDraw.Draw(imd)

draw.line((0, 0) + imd.size, fill=128)                  #划线
draw.line((0, imd.size[1], imd.size[0], 0), fill=128)

# 直线:line([x1,y1（起点）,x2,y2] ,options)
# 圆弧:arc([x1, y1（左上角坐标）, x2, y2(右下角坐标)],  startAngle,  endAngle,  options)
# 圆和椭圆：ellipse([x1,y1,x2,y2],  options)
# 弦:chord([x1, y1, x2, y2],  startAngle,  endAngle,  options)
# 扇形:pieslice([x1,y1,x2,y2],  startAngle,  endAngle,  options)
# 多边形:polygon(([x1,y1,x2,y2，…],options)
# 矩形:rectangle([x1,y1,x2,y2],options)
# 文字:text(position,  string,  options)
# 字符串大小:textsize(string,  options)
# draw.ink = 0(R) + 0(G) * 256 + 0(B) * 256 * 256
draw.ink = 255 + 0 * 256 + 0 * 256 * 256       #红色(画笔颜色)

fontsize = ImageFont.truetype("C:\Windows\Fonts\Arial.ttf", 36)
draw.text([100, 240], 'a beautiful girl', font=fontsize)
imd.save('../pillowImages/star.jpg', "jpeg")

# 透明度文字
opcityImg = Image.open('../images/star.jpg').convert('RGBA')
txt = Image.new('RGBA', opcityImg.size, (255, 255, 255, 0))
d = ImageDraw.Draw(txt)
d.text((100,10), "Hello", font=fontsize, fill=(255, 255, 255, 128))
out = Image.alpha_composite(opcityImg, txt)
out.save('../pillowImages/star_opacity.jpg', "bmp")

