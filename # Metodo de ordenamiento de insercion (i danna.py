# Metodo de ordenamiento de insercion (insertionSort)
from random import sample 

# Crea una lista base del 0 al 99
lista = list(range(100)) 
# Selecciona 8 números al azar de la lista anterior
vectorins = sample(lista, 8) 

def insertionsort(vectorins):
    """Esta función ordenará el vector que le pases como argumento con el método insertion Sort"""
    print("el vector a ordenar con insercion es:", vectorins)
    
    # Calculamos el tamaño del vector (corregido: len nos da la cantidad de elementos)
    largo = len(vectorins) 

    # Recorremos el vector desde el segundo elemento (índice 1) hasta el final
    for i in range(1, largo):
        # Guardamos el valor actual que queremos "insertar" en la posición correcta
        elemento = vectorins[i]
        # Empezamos a comparar con el elemento justo a la izquierda
        j = i - 1