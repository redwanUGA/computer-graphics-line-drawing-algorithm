from compgraph import basic_alg, brz
import cv2
import numpy as np
import random as rd
N = input('enter number of lines: \n ')
alg = input('select algorithm \n 1. Basic \n 2.Brezenham \n : ')
black_screen = np.zeros((501,501))
if alg == '1':
    for i in range(1,int(N)):
        black_screen = basic_alg(rd.randint(1,500), rd.randint(1,500), rd.randint(1,500), rd.randint(1,500), black_screen)
elif alg == '2':
    for i in range(1,int(N)):
        black_screen = brz(rd.randint(1,500), rd.randint(1,500), rd.randint(1,500), rd.randint(1,500), black_screen)


cv2.imshow('image', black_screen)
cv2.waitKey()
cv2.destroyAllWindows()