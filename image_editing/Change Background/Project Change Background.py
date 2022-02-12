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

# Only accept the condition that the size of person image is smaller than the background image
# in both height and width
def change_background(img, new_background, replace_color):  
	w_img = len(img[0])
	h_img = len(img)
	w_background = len(new_background[0])
	h_background = len(new_background)
	if w_background > w_img and h_background > h_img:
		for i in range(h_img):
			for j in range(w_img):
				threshold = color_distance(new_background[i][j], replace_color)
		       		input_distance = color_distance(img[i][j], new_background[i][j])
				if input_distance - threshold > -180 and input_distance - threshold < -30:
					img[i][j] = new_background[i][j]
	return save(img, 'name of destination png file')

def color_distance(color1, color2):
	r1, g1, b1 = color1
	r2, g2, b2 = color2
	return ((r1 - r2)**2 + (g1 - g2)**2 + (b1 - b2)**2)**0.5

image = convert('person image name')
new_background = convert('background image name')
change_background(image, new_background, (0, 255, 0))
