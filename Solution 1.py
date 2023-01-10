# No Borrar
testResults = [ True, True, True, True, True, False, False, False, False, False, False, False ]

resultado = None

# Escribe aquí tu algoritmo - guarda el resultado

resultado = 0
for e in testResults:
    if not(e):
        break
    resultado += 1

print(resultado)