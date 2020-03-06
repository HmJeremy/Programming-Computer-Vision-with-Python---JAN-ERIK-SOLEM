from PIL import Image
#from pylab import *
from numpy import *

im = array(Image.open('hmj.jpg').convert('L'))

im2 = 255 - im #invert image
im3 = (100.0/255) * im + 100 #clamp to interval 100...200
im4 = 255.0 * (im/255.0)**2 #squared

print(int(im.min()), int(im.max()))
print(int(im2.min()), int(im2.max()))
print(int(im3.min()), int(im3.max()))
print(int(im4.min()), int(im4.max()))

#pil_im = Image.fromarray(im3)
#pil_im = Image.fromarray(uint8(im4))

imshow(im4)

show()