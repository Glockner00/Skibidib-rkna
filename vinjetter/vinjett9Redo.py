import matplotlib.pyplot as plt
import matplotlib.image as img


picture = img.imread('bild.jpg')
x1, y1 = 80, 100
x2, y2 = 180, 210

square = picture[y1:y2, x1:x2, :]

square[:, :, 0] = 255
square[:, :, 1] = 166
square[:, :, 2] = 0
plt.imshow(picture)
plt.show()



