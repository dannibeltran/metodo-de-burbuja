#Metodo de ordenamiento de seleccion (selectionSort)
# Importa la función sample del módulo random
# Sirve para obtener una muestra aleatoria de elementos
from random import sample

# Crea una lista con números del 0 al 99
lista = list(range(100))

# Genera un vector con 8 números aleatorios sin repetir
vectorselect = sample(lista, 8)

# Definición de la función selectionsort
def selectionsort(vectorselect):
    """
    Esta función ordena el vector usando el método de selección (Selection Sort)
    """

    # Muestra el vector original
    print("El vector a ordenar es:", vectorselect)

    # Calcula la longitud del vector
    largo = len(vectorselect)

    # Recorre cada posición del vector
    for i in range(largo):

        # Asume que el elemento actual es el mínimo
        minimo = i

        # Busca el elemento más pequeño en el resto del vector
        for j in range(i + 1, largo):
            if vectorselect[minimo] > vectorselect[j]:
                minimo = j  # Actualiza la posición del mínimo

        # Intercambia el elemento actual con el mínimo encontrado
        vectorselect[i], vectorselect[minimo] = vectorselect[minimo], vectorselect[i]

    # Muestra el vector ya ordenado
    print("El vector ordenado es:", vectorselect)


# Llama a la función para ordenar el vector
selectionsort(vectorselect)