import sudokuAlg as sud
import numpy as np

sudokuM = np.array([
    [0, 0, 5,  3, 6, 0,  4, 0, 0],
    [9, 6, 2,  0, 0, 4,  0, 7, 0],
    [3, 0, 4,  0, 2, 9,  0, 6, 0],
    
    [8, 2, 0,  9, 4, 0,  0, 1, 3],
    [0, 4, 9,  0, 3, 0,  0, 5, 7],
    [0, 0, 0,  2, 0, 0,  9, 8, 0],

    [4, 0, 6,  0, 0, 1,  0, 0, 2],
    [0, 0, 0,  6, 9, 3,  0, 0, 5],
    [0, 0, 3,  0, 8, 0,  0, 0, 0]], dtype=np.int8)

solvedBoard = sud.mainRuntime(sudokuM)
# gives cmd-line output. 
