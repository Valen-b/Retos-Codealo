import random
# No borrar
A = [1, 2, 3, 4, 5]
B = [6, 7, 8, 9, 10]

completado = True #Cambiar a true cuando este completado

# Implementación
C = []

def shuffle(arr1, arr2):
    lA = len(A)
    lB = len(B)
    cA = 0
    cB = 0

    while 1:
        
        if cA < lA and cB < lB:
            r = random.randint(0,1)
            if r==0:
                C.append(A[cA])
                cA += 1
            else:
                C.append(B[cB])
                cB += 1
        elif cA < lA:
            C.append(A[cA])
            cA += 1
        else:
            C.append(B[cB])
            cB += 1

        if cA+cB==lA+lB:
            return C
            break
C = shuffle(A, B)


print(completado)