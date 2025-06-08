import random
from time import sleep

lista = 'ABCDEFGHIJLMNOPQRSTUV'
b = s = 0

while True:
    a = random.randint(0,20)
    print(lista[a])
    x =input()
    
    if x.lower() == "b":
        b += 1
    if x.lower() == "s":
        s += 1
    
    print(f"Sávio: {s}\nByanca: {b}")