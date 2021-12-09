def convert(filename):
    img = Image.open(filename)
    pil_img = img.convert('RGB')
    arr = np.array(pil_img.getdata(), dtype=np.uint8).reshape(pil_img.height, pil_img.width, 3)
    return [ [ (int(p[0]),int(p[1]),int(p[2])) for p in row ] for row in arr ]

def save(img, filename):
    arr = np.asarray(img, dtype=np.uint8)
    pil_img = Image.fromarray(arr)
    pil_img.save(filename, format='png')

def check(image, col_index, row_index, region_height, region_width):
    if col_index < 0 or row_index < 0 or region_height < 0 or region_width < 0:
        return False 
    if (row_index + region_height) > len(image) or row_index >= len(image):
        return False 
    if (col_index + region_width) > len(image[0]) or col_index >= len(image[0]):
        return False
    return True          


def flip_vertical(image, col_index, row_index, region_height, region_width):
    if not check(image, col_index, row_index, region_height, region_width):
        continue
    else:
        for row in range(row_index, row_index + region_height//2): 
            for column in range(col_index,col_index + region_width):
                temp = image[row][column] 
                image[row][column] = image[2*row_index + region_height - row - 1][column]
                image[2*row_index + region_height - row - 1][column] = temp        
    

image = convert('person image name')
flip_vertical(image, 0, 0, 200, 200)
save(image, 'output_file.png')