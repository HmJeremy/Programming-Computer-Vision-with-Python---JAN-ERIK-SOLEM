from PIL import Image
from pylab import *

im = array(Image.open('hmj.jpg').convert('L'))

figure()
# don’t use colors
gray()
# show contours with origin upper left corner
contour(im, origin='image')

axis('equal')
axis('off')

figure()

hist(im.flatten(),128)

show()