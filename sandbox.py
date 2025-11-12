'''
Código Fuente (2%)
● Implementación de algoritmos ineficientes: Correcta simulación de la versión actual.
● Implementación optimizada: Algoritmos más eficientes.
● Generación de dataset: Dataset realista y utilizable.
● Graficación de resultados: Correcta y bien presentada.
● Módulo de grafos: Funcional y con salida medible.
● Utilización de las herramientas solicitadas.
● Estructuras, modularidad, reglas básicas de Python.
● Funcionalidad completa.
'''

''' 1. Generar un dataset funcional de usuarios, series/películas y lo que necesite con pandas y numpy. Este es simulado y manejables (10000 registros) '''
'''
La profe dice que: 1. 10000 registros en total y con respecto a esto usuarios, películas y "lo que necesite" es porque dependiendo de lo que usted quiera realizar, 
por ejemplo puede ser una tabla ranking usando valores para estrellas (favorito) o va depender de los datos que usted necesite.
'''
'''
2. Desarrollar los algoritmos que simulan la versión que actualmente (use algoritmos poco eficientes) está usando la compañía Patito para las funcionalidades de:
a) Ordenamiento del dataset
b) Búsqueda por nombre de serie,
c) Búsqueda por similitud de texto de película.
'''

# a) Bubble Sort. (Tomado de la presentacion de 'Algoritmos de Ordenamiento'). (Algoritmo Ineficiente).
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if str(arr[j]).lower() > str(arr[j + 1]).lower():
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
#Sea cambio para que no haya problemas entre int y strings

# Llamado
arreglo = [64, 34, 25, 12]
bubble_sort(arreglo)
print("Arreglo ordenado con Bubble Sort:", arreglo)

# b) Busqueda Lineal. (Tomado de la presentacion de 'Algoritmos de Busqueda'). (Algoritmo Ineficiente).
def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

# numeros = [10, 25, 30, 45, 50]
# buscar = 45
# resultado = busqueda_lineal(numeros, buscar)

# print("Resultado de la búsqueda:", resultado)

# c) Fuerza bruta. (Tomado de la presentacion de 'Procesamiento de Cadenas'). (Algoritmo Ineficiente).
def naive_search(lista, pattern):
    #Ignora mayúsculas y minúsculas.
    #Busca coincidencias exactas o parciales dentro de cada texto de una lista.


    comparisons = 0
    encontrados = []
    pattern = pattern.lower()

    # Recorre cada elemento de la lista
    for text in lista:
        text = str(text).lower()
        n = len(text)
        m = len(pattern)

        for start in range(n - m + 1):
            i = start
            j = 0

            # Comparar carácter por carácter
            while j < m and text[i] == pattern[j]:
                comparisons += 1
                i += 1
                j += 1

            if j < m:
                comparisons += 1

            # Si el patrón completo fue encontrado en el texto
            if j == m:
                encontrados.append(text)
                break  # pasa al siguiente texto

    # Mostrar resultados
    if encontrados:
        print(" Se han encontrado las siguientes coincidencias:\n")
        for e in encontrados:
            print(" -", e)
    else:
        print("No se encontró ninguna coincidencia.")

    print(f"\nTotal comparisons: {comparisons}")


''' 3. Analizar los algoritmos del sistema actual e identificar su complejidad temporal en notación Big-O.'''

    # Bubble Sort es un algotimo que requiere un tiempo cuadratico, y en el mejor de los casos es lineal. Big O(n^2)
    # Busqueda Lineal tiene complejidad O(n) en el peor caso y O(1) si el elemento se encuentra en la primera posicion.
    # Fuerza Bruta tiene una complejidad de O(n*m) en el peor caso y O(n) en el mejor caso.

'''4. Implementar versiones optimizadas de los algoritmos de ordenamiento y búsqueda, mencionados en el punto 2. Deben ser codificados.'''

# Merge Sort: (Tomado de la presentacion 'Algoritmos de Ordenacion') (Algoritmo Eficiente)
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

# # Ejemplo de uso
# nums = [38, 27, 43, 3, 9, 82, 10]
# print("Arreglo ordenado con Merge Sort:", merge_sort(nums))

# Binary Search: (Tomado de la presentacion 'Algoritmos de Busqueda') (Algoritmo Eficiente)
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

def busqueda_binaria_main(lista,objetivo):
    inicio = 0
    fin = len(lista) - 1
    objetivo = objetivo.lower()

    while inicio <= fin:
        medio = (inicio + fin) // 2
        elemento = str(lista[medio]).lower()

        if elemento == objetivo:
            return medio
        elif elemento < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1


# # Ejemplo de uso
# numeros = [10, 20, 30, 40, 50, 60, 70]
# buscar = 40
# resultado = busqueda_binaria(numeros, buscar)

# if resultado != -1:
#     print(f"Elemento encontrado en el índice {resultado}")
# else:
#     print("Elemento no encontrado")


# Algotirmo Boyer Moore Horspool (Tomado de la presentacion de 'Procesamiento de cadenas') (Algoritmo Eficiente)
def build_shift_table(pattern):
    m = len(pattern)
    table = {}

    # Construcción de la tabla de desplazamientos
    for i in range(m - 1):
        table[pattern[i]] = m - 1 - i

    # Valor por defecto si el carácter no está en el patrón
    table['*'] = m
    return table


def horspool_search(text, pattern):
    m = len(pattern)
    n = len(text)
    table = build_shift_table(pattern)

    print("Tabla de desplazamientos:", table)

    k = m - 1
    while k < n:
        i = 0
        while i < m and pattern[m - 1 - i] == text[k - i]:
            i += 1
        if i == m:
            print("Patrón encontrado en la posición", k - m + 1)
            return k - m + 1
        else:
            mismatched_char = text[k]
            shift = table.get(mismatched_char, table['*'])
            print(f"No coincide en posición {k}. Carácter: '{mismatched_char}' → mover {shift} posiciones.")
            k += shift

    print("No se encontró el patrón en el texto.")
    return -1

def horspool_search_Main(text, pattern): #El horspool para el main
    m = len(pattern)
    n = len(text)
    table = build_shift_table(pattern)

    k = m - 1
    while k < n:
        i = 0
        while i < m and pattern[m - 1 - i] == text[k - i]:
            i += 1
        if i == m:
            return k - m + 1
        else:
            mismatched_char = text[k]
            shift = table.get(mismatched_char, table['*'])
            k += shift
    return -1

# # Ejemplo de uso
# texto = "Este es un ejemplo de búsqueda con Horspool"
# patron = "ejemplo"

# horspool_search(texto, patron)


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


    #Boyer-Moore Horspool: Tiene una complejidad promedio O(n/m).
        # Por qué?
            # Aprovecha desplazamientos inteligentes basados en el carácter que no coincide.
            # En la práctica suele ser más rápido que otros algoritmos porque evita comparar carácter por carácter.
            # Es ideal para textos largos y patrones relativamente cortos.
            # Aunque su peor caso es O(n*m), rara vez ocurre, por lo que se considera muy eficiente en escenarios reales.

''' 6. Medir y comparar tiempos de ejecución de ambas versiones (actual de la empresa y la optimizada por ustedes) con time o timeit.''' 
# Medir algoritmos eficientes e ineficientes con el df.  Lo mismo de la investigacion.

'''7. Graficar los resultados con matplotlib.'''
#  Lo mismo de la investigacion. 

''' 8. Implementar un módulo de grafos que resuelva un problema de negocio, para ello cree un código y que permita ver un resultado medible. Ejemplo: poder visualizar las preferencias de los clientes. '''

# La profe dice que: Se necesita investigar sobre Grafos y sí ocupa código y sí se necesita algo visual (para la parte medible) por ejemplo una gráfica.



