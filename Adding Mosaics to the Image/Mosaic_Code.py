import numpy as np
from PIL import Image

def convert(filename):
    img = Image.open(filename)
    pil_img = img.convert('RGB')
    arr_img = np.array(pil_img.getdata(), dtype=np.uint8).reshape(pil_img.height, pil_img.width, 3)
    l = []
    for row in arr_img:
        col = []
        for pixel in row:
            col.append((int(pixel[0]),int(pixel[1]),int(pixel[2]))
        l.append(col)
    return l

def save(img, filename):
    arr = np.asarray(img, dtype=np.uint8)
    pil_img = Image.fromarray(arr)
    pil_img.save(filename, format='png')

def pixelization(image, length, percentage_change):
    for i in range(0, len(image), length):
        for j in range(len(image[0]) - 1, int((1 - percentage_change*0.01)*len(image[0])), -length):
            r = 0
            g = 0
            b = 0
            for ii in range(i, i + length):
                for jj in range(j, j - length, -1):
                    r += image[ii][jj][0]
                    g += image[ii][jj][1]
                    b += image[ii][jj][2]
            new_r = r/(length)**2
            new_g = g/(length)**2
            new_b = b/(length)**2
            for ii in range(i, i + length):
                for jj in range(j, j - length, -1):
                    image[ii][jj] = (int(new_r), int(new_g), int(new_b))
                    
                    
image = convert('input image name')
pixelization(image, 10, 60)
save(image, 'output_file.png')


