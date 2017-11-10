from PIL import Image, ImageChops
# 对图像的算术操作

# 1.constant(image,value) ⇒ image 返回一个和给定图像尺寸一样的一层，该层被给定的像素值填充。
im = Image.open('images/star2.jpg')
im.getpixel((0, 0))
image = ImageChops.constant(im, 128)
# image.show()

# 2.(image) ⇒ image 返回给定图像的拷贝。
# ImageChops.duplicate(im).show()


# 3.invert(image) ⇒ image 返回最大值255减去当前值的图像。
# ImageChops.invert(im).show()

# 4.lighter(image1, image2) ⇒ image 逐像素比较，选择较大值作为新图像的像素值。
im02 = Image.open('images/nature.jpg')
# ImageChops.lighter(im, im02).show()

# 5.darker(image1,image2) ⇒ image
# ImageChops.darker(im, im02).show()

#6.difference(image1, image2) ⇒ image 返回两幅图像逐像素差的绝对值形成的图像。
# ImageChops.difference(im, im02).show()

# 7.multiply(image1, image2) ⇒ image  Superimposes twoimages on top of each other.如果与一张纯黑图片相乘，其结果是黑色的。如果与一张纯白图像相乘，其结果是不确定的。
# out = image1 *image2 / MAX
# ImageChops.multiply(im, im02).show()

# 8.screen(image1,image2) ⇒ image     out = MAX -((MAX - image1) * (MAX - image2) / MAX)
# ImageChops.screen(im, im02).show()

# 9.add(image1,image2, scale, offset) ⇒ image   out = (image1 +image2) / scale + offset
# 两个图像对应像素值相加，然后除以变量offset，并且再加上变量offset。如果忽略，变量scale为1.0，变量offset为0.0。
# ImageChops.add(im, im02, 2, 10).show()

#10.subtract(image1, image2, scale, offset) ⇒ image   out = (image1 -image2) / scale + offset
# ImageChops.subtract(im, im02, 1, -10).show()

# 11.blend(image1, image2, alpha) ⇒ image   与Image模块中的函数blend()一样，根据变量alpha合成两张图像。
# ImageChops.blend(im, im02, 0.7).show()

# 12.composite(image1, image2, mask) ⇒ image  与Image模块中的函数composite()一样，根据变量mask合成两张图像。变量  mask的模式为“1”，“L”或者“RGBA”。这三个参数的尺寸必须一样大。
# r, g, b = im.split()
# ImageChops.composite(im, im02, r).show()
# ImageChops.composite(im, im02, g).show()
# ImageChops.composite(im, im02, b).show()

#13.offset(image,xoffset, yoffset) ⇒ image  返回一个图像数据按照变量offset做了偏移的图像。Datawraps around the edges.如果变量yoffset缺省，它被假设与变量xoffset一样。
#ImageChops.offset(im02, 100).show()


