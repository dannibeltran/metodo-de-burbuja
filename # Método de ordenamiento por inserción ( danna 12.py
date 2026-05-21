# Método de ordenamiento por inserción (Insertion Sort)

# Importa la función sample para generar números aleatorios sin repetición
from random import sample

# Crea una lista del 0 al 99
lista = list(range(100))

# Genera un vector de 8 elementos aleatorios
vectorins = sample(lista, 8)

# Definición de la función de ordenamiento por inserción
def insertion(vectorins):
    """Esta función ordena el vector usando el método Insertion Sort"""

    # Muestra el vector original
    print("El vector a ordenar con inserción es:", vectorins)

    # Recorre el vector desde el segundo elemento (índice 1)
    for i in range(1, len(vectorins)):

        # Guarda el valor actual que se quiere insertar en la parte ordenada
        elemento = vectorins[i]

        # Índice del elemento anterior
        j = i - 1

        # Desplaza los elementos mayores hacia la derecha
        while j >= 0 and elemento < vectorins[j]:
            vectorins[j + 1] = vectorins[j]
            j -= 1

        # Inserta el elemento en su posición correcta
        vectorins[j + 1] = elemento

    # Muestra el vector ya ordenado
    print("El vector ordenado con inserción es:", vectorins)

# Llamada a la función
insertion(vectorins)