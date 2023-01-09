# No Borrar
a1 = [ 3, 1, 2, 8, 13, 9, 1, 1, 2, 3, 4, 10, 12, 11, 1, 1]
a2 = [ 5, 7, 7, 7, 7, 2, 1, 2, 0]

resultado = 0;


# Escribe tu algoritmo - guarda en resultado

def find_max(arg):
    max = arg[0]
    for e in arg:
        if e > max:
            max = e
    return max

resultado = find_max(a1) * find_max(a2)

print(resultado)