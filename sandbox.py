''' 1. Generar un dataset funcional de usuarios, series/películas y lo que necesite con pandas y numpy. Este es simulado y manejables (10000 registros) '''
# Facil, pero hay que preguntarle a la profe que columnas usar, porque no especifica que variables debe tener el df.

'''
2. Desarrollar los algoritmos que simulan la versión que actualmente (use algoritmos poco eficientes) está usando la compañía Patito para las funcionalidades de:
a) Ordenamiento del dataset
b) Búsqueda por nombre de serie,
c) Búsqueda por similitud de texto de película.
'''

# a) Bubble Sort. (Tomado de la presentacion de 'Algoritmos de Ordenamiento').
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Llamado
arreglo = [64, 34, 25, 12]
bubble_sort(arreglo)
print("Arreglo ordenado con Bubble Sort:", arreglo)

# b) Busqueda Lineal. (Tomado de la presentacion de 'Algoritmos de Busqueda').
def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

numeros = [10, 25, 30, 45, 50]
buscar = 45
resultado = busqueda_lineal(numeros, buscar)

print("Resultado de la búsqueda:", resultado)

# c) Fuerza bruta. (Tomado de la presentacion de 'Procesamiento de Cadenas').
def naive_search(text, pattern):
    n = len(text)
    m = len(pattern)
    comparisons = 0

    for start in range(n - m + 1):
        i = start  # posición en el texto
        j = 0      # posición en el patrón

        while j < m and text[i] == pattern[j]:
            comparisons += 1
            i += 1
            j += 1

        if j < m:
            comparisons += 1

        if j == m:
            print(f"Pattern found at index {start}")

    print(f"Total comparisons: {comparisons}")

''' 3. Analizar los algoritmos del sistema actual e identificar su complejidad temporal en notación Big-O.'''

    # Bubble Sort es un algotimo que requiere un tiempo cuadratico, y en el mejor de los casos es lineal. Big O(n^2)
    # Busqueda Lineal tiene complejidad O(n) en el peor caso y O(1) si el elemento se encuentra en la primera posicion.
    # Fuerza Bruta tiene una complejidad de O(n*m) en el peor caso y O(n) en el mejor caso.

'''4. Implementar versiones optimizadas de los algoritmos de ordenamiento y búsqueda, mencionados en el punto 2. Deben ser codificados.'''

# Merge Sort: (Tomado de la presentacion 'Algoritmos de Ordenacion')
def merge_sort(arr):
    if len(arr) < 2:
        return arr

    # Dividir
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Combinar
    return merge(left, right)

def merge(left, right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    # Agregar los elementos restantes
    result.extend(left)
    result.extend(right)

    return result

# Ejemplo de uso
nums = [38, 27, 43, 3, 9, 82, 10]
print("Arreglo ordenado con Merge Sort:", merge_sort(nums))

# Binary Search: (Tomado de la presentacion 'Algoritmos de Busqueda')
def busqueda_binaria(lista, objetivo):
    inicio = 0
    fin = len(lista) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1

# Ejemplo de uso
numeros = [10, 20, 30, 40, 50, 60, 70]
buscar = 40
resultado = busqueda_binaria(numeros, buscar)

if resultado != -1:
    print(f"Elemento encontrado en el índice {resultado}")
else:
    print("Elemento no encontrado")


'''5. Especificar su nueva notación y la razón que justifique la escogencia de sus algoritmos para cada caso.''' 
    # Merger Sort: Es un algoritmo que requiere un tiempo logaritmico-lineal. Big O (n log(n)) 
        # Por que?
            # Es ideal cuando se trabaja con listas muy grandes. 
            # Siempre corre en O(n\log n), incluso en el peor caso.



    # Binary Search: Tiene una complejidad en el peor caso de O(log (n)) y en el mejor caso de un O(1).
        # Por que? 
            # Consume menos memoria (no hay llamadas recursivas en la pila).
            # Suele ser más rápido en la práctica porque evita la sobrecarga de la recursión.
            # Aunque funciona con listas ordenada, permite búsquedas rápidas y confiables

''' 6. Medir y comparar tiempos de ejecución de ambas versiones (actual de la empresa y la optimizada por ustedes) con time o timeit.''' 
# Aqui va el codigo del Laboratorio 3, pero primero hay que crear el df pero hay que preguntarle a la profe que columnas usar, porque no especifica que variables debe tener el df. . 

'''7. Graficar los resultados con matplotlib.'''
#  Aqui tambien va el codigo del Laboratorio 3, pero primero hay que crear el dfpero hay que preguntarle a la profe que columnas usar, porque no especifica que variables debe tener el df. . 

''' 8. Implementar un módulo de grafos que resuelva un problema de negocio, para ello cree un código y que permita ver un resultado medible. Ejemplo: poder visualizar las preferencias de los clientes. '''

# Tengo que consultarle a la profe el lunes que diablos es esto. 
