#Implementación en Python y utiliza el debugger para asegurarte que funciona adecuadamente y entiendes su funcionamiento.

def algoritmoBurbuja(ejemplo):
    numero = len(ejemplo)
    for i in range(numero-1):       # bucle padre
        for j in range(numero-1-i): # bucle hijo
            if ejemplo[j] > ejemplo[j+1]:
                ejemplo[j], ejemplo[j+1] = ejemplo[j+1], ejemplo[j]

lista = [28,4,255,1]
algoritmoBurbuja(lista)

print(lista)