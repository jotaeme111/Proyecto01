import pandas as pd
import time
from sandbox_editado import bubble_sort, busqueda_lineal, naive_search
import matplotlib.pyplot as plt

df = pd.read_excel("dataset.xlsx")
valores = df['title'].astype(str).tolist()[:1000]

print("Algoritmos ineficientes")

tiempos = {}

inicio = time.time()
bubble_sort(valores)
fin = time.time()
tiempos['Bubble Sort'] = fin - inicio
print(f"Bubble Sort: {fin - inicio:.4f} segundos")

while True:
    try:
        busqueda = input(" Ingrese el título o parte del título que desea buscar, o ingrese enter para salir: ").strip()
        if not busqueda:
            print('Programa finalizado.')
            break

        inicio = time.time()
        indice = busqueda_lineal(valores, busqueda)
        fin = time.time()
        tiempos['Búsqueda Lineal'] = fin - inicio

        if indice != -1:
            print(f"\n'{busqueda}' encontrado exactamente en la posición {indice}")
        else:
            print(f"\n'{busqueda}' no encontrado exactamente, buscando similitudes\n")
            inicio = time.time()
            naive_search(valores, busqueda)
            fin = time.time()
            tiempos['Búsqueda Naive'] = fin - inicio

        print(f"\nTiempo total de búsqueda: {fin - inicio:.4f} segundos")
    except ValueError as e:
        print(e)

if tiempos:
    plt.figure(figsize=(8, 5))
    plt.bar(tiempos.keys(), tiempos.values(), color=['#E57373', '#FFD54F', '#81C784'])
    plt.title("Comparación de tiempos - Algoritmos Ineficientes")
    plt.ylabel("Tiempo (segundos)")
    plt.xlabel("Algoritmo")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()
