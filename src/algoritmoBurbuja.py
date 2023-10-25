#Implementación en Python y utiliza el debugger para asegurarte que funciona adecuadamente y entiendes su funcionamiento.


def algoritmoBurbuja(lista):
    numero = len(lista)
    for i in range(numero-1):       # bucle padre
        for j in range(numero-1-i): # bucle hijo
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

if __name__=="__main__":
    #entrada
    lista = [28,4,255,1]
    #proceso
    algoritmoBurbuja(lista)
    #salida
    print(lista)