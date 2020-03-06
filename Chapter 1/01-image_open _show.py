from PIL import Image
from pylab import *


im = array(Image.open("hmj.jpg"))
#im = array(Image.open("hmj.jpg").convert('L'))

imshow(im)

title('plotting: "hmj.jpg"')

#axis('off')

show()