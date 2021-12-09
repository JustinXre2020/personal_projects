def convert(filename):
    img = Image.open(filename)
    pil_img = img.convert('RGB')
    arr = np.array(pil_img.getdata(), dtype=np.uint8).reshape(pil_img.height, pil_img.width, 3)
    return [ [ (int(p[0]),int(p[1]),int(p[2])) for p in row ] for row in arr ]

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
                    
                    
image = convert('person image name')
pixelization(image, 10, 60)
save(image, 'output_file.png')


