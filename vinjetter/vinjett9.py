import matplotlib.pyplot as plt
import matplotlib.image as img
import numpy as np


def image():
    image_name = 'bild.jpg'
    im_data = img.imread(image_name)

    print(im_data)
    print(np.shape(im_data))

    cmap = 'hot'
    plt.imshow(im_data, cmap=cmap, interpolation='nearest')
    plt.show()
    

    d = [im_data[x] for x in range(300, 400)]
    print(d)

    red_data = im_data[:,:,0] 
    green_data = im_data[:,:,1]
    blue_data = im_data[:,:,2]

    image1 = np.array([blue_data, green_data, red_data]) 
    image1 = np.swapaxes(image1, 0, 1)
    image1 = np.swapaxes(image1, 1, 2)
    print(image1)
    print(np.shape(image1))
    
    cmap = 'hot'
    plt.imshow(image1, cmap=cmap, interpolation='nearest')
    plt.show()
    

image()



    

