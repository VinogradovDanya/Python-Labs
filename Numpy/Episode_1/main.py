from PIL import Image
import numpy as np

for i in range(1, 4):
    im = Image.open('lunar0' + str(i) + '_raw.jpg')
    data = np.array(im)

    M = data.max()
    m = data.min()
    data = (data - m)
    data = (255 / (M - m)) * data
    data = data.astype('uint8')

    res_img = Image.fromarray(data)
    res_img.save('lunar0' + str(i) + '.jpg')
