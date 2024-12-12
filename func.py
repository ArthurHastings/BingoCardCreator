import numpy as np
import random
from images_list import images_list

def randomizeMatrix(n, m, list):
    matrix_size = (n, m)
    matrix = np.zeros(matrix_size)
    random.shuffle(list)

    matrix = np.array(list).reshape(matrix_size)
    
    return matrix

# print(randomizeMatrix(n, m, images_list))
