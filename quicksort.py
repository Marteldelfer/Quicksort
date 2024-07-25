#Autoral
#Muito mais eficiênte que ordenação por seleção, porém tem um limite de recursão


from random import randint as rand
from time import time
lista = [rand(1,10) for i in range(990)]

start = time()

def quicksort(lista: list) -> list:
    listaesq = []
    listadir = []
    if lista == []:
        return []
    num = lista.pop()
    for i in lista:
        if i <= num:
            listaesq.append(i)
        else:
            listadir.append(i)
    return quicksort(listaesq) + [num] + quicksort(listadir)

print(quicksort(lista))
print(time() - start)