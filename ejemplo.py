from site import removeduppaths
from turtle import color



import random

colores = ["Red", "Blue", "Yellow", "Green", "Orange", "Violet"]
def recursiva(lista):
    
    for i in range(len(colores)):
        i = random.randint(0, len(colores)-1)
    if i % 2 == 0:
        print(colores[i])
    else:
        recursiva(colores)
            
recursiva(colores)

