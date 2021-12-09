from CSE8AImage import *

def pixelization(image, square_size, column_percentage):
    # TODO
    for row in range(0, height(image), square_size):
        for column in range(width(image) - 1, int((1 - column_percentage*0.01)*width(image)), -square_size):
            r = 0
            g = 0
            b = 0
            for sub_row in range(row, row + square_size):
                for sub_col in range(column, column - square_size, -1):
                    r += image[sub_row][sub_col][0]
                    g += image[sub_row][sub_col][1]
                    b += image[sub_row][sub_col][2]
            new_r = r/(square_size)**2
            new_g = g/(square_size)**2
            new_b = b/(square_size)**2
            for sub_row in range(row, row + square_size):
                for sub_col in range(column, column - square_size, -1):
                    image[sub_row][sub_col] = (int(new_r), int(new_g), int(new_b))

image = load_img('input.png')
pixelization(image, 10, 60)
save_img(image, 'pixelized.png')


