# Método de ordenamiento de la Burbuja ascendente (Bubble Sort)

# Importa la función sample para generar números aleatorios sin repetición
from random import sample

# Crea una lista del 0 al 99
lista = list(range(100))

# Genera un vector de 8 elementos aleatorios a partir de la lista
vectorbs = sample(lista, 8)

# Definición de la función Bubble Sort
def bubblestort(vectorbs):
    """Esta función ordena el vector usando el método Bubble Sort"""

    # Muestra el vector original
    print("El vector a ordenar es:", vectorbs)

    # Obtiene la longitud del vector
    n = len(vectorbs)

    # Recorre todo el vector
    for i in range(n):
        
        # Recorre el vector comparando elementos adyacentes
        for j in range(0, n - i - 1):
            
            # Compara elementos consecutivos
            if vectorbs[j] > vectorbs[j + 1]:
                
                # Intercambia los elementos si están en el orden incorrecto
                vectorbs[j], vectorbs[j + 1] = vectorbs[j + 1], vectorbs[j]

    # Muestra el vector ya ordenado
    print("El vector ordenado es:", vectorbs)

# Llamada a la función para ordenar el vector
bubblestort(vectorbs)
                    