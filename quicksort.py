#Autoral
#Muito mais eficiênte que ordenação por seleção, porém tem um limite de recursão

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

if __name__ == "__main__":
    from random import randint as rand
    from time import time
    
    lista = [rand(1,10) for i in range(990)]
    start = time()
    print(quicksort(lista))
    print(time() - start)
