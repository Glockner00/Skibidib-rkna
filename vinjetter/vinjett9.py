import matplotlib.pyplot as plt
import matplotlib.image as img

image = img.imread('bild.jpg')
image2 = img.imread('eyes.jpg')

plt.imshow(image)

h, w, _ = image2.shape
new_h = h // 10
new_w = w // 10

image2_resized = image2[:new_h, :new_w]


plt.imshow(image2_resized, extent=[100,300,100,300])

plt.show()
