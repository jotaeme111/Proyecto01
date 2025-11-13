import pandas as pd
import time
import numpy as np
import matplotlib.pyplot as plt
from sandbox import (
    bubble_sort,
    busqueda_lineal,
    naive_search,
    merge_sort,
    busqueda_binaria_main,
    horspool_search_Main
)

df = pd.read_excel("dataset.xlsx")
valores_base = df['title'].astype(str).str.lower().tolist()[:6138]

valores_inef = valores_base.copy()
valores_ef = valores_base.copy()

tiempos_inef = {}
tiempos_ef = {}

print("Algoritmos ineficientes y eficientes")

inicio = time.time()
bubble_sort(valores_inef)
fin = time.time()
tiempos_inef["Bubble Sort"] = fin - inicio
print(f"Bubble Sort: {fin - inicio:.4f} segundos")

inicio = time.time()
valores_ef = merge_sort(valores_ef)
fin = time.time()
tiempos_ef["Merge Sort"] = fin - inicio
print(f"Merge Sort completado en: {fin - inicio:.4f} segundos")

while True:
    busqueda = input("Ingrese el título o parte del título que desea buscar, o toque enter para salir: ").strip().lower()
    if not busqueda:
        print("\nPrograma finalizado.")
        break

    print("\nResultados con algoritmos ineficientes:")

    inicio = time.time()
    indice = busqueda_lineal(valores_ef, busqueda)
    fin = time.time()
    total= fin-inicio
    tiempos_inef["Búsqueda Lineal"] = total
    print(fin-inicio)

    if indice != -1:
        print(f"\n'{busqueda}' encontrado exactamente en la posición {indice}")
        print(f"Tiempo de búsqueda lineal: {fin - inicio:.6f} segundos\n")
        tiempos_inef["Búsqueda Lineal"] = fin-inicio
    else:
        print(f"\n'{busqueda}' no encontrado exactamente, buscando similitudes\n")
        inicio = time.time()
        naive_search(valores_inef, busqueda)
        fin = time.time()
        tiempos_inef["Naive Search"] = fin - inicio
        print(f"\nTiempo total de búsqueda con Naive Search: {fin - inicio:.6f} segundos\n")

    print("Resultados con algoritmos eficientes:")

    inicio = time.time()
    indice = busqueda_binaria_main(valores_ef, busqueda)
    fin = time.time()
    tiempos_ef["Búsqueda Binaria"] = fin - inicio

    if indice != -1:
        print(f"\nCoincidencia exacta encontrada:")
        print(f" {valores_ef[indice]}")
        print(f"Tiempo de búsqueda binaria: {fin - inicio:.6f} segundos\n")
        tiempos_ef["Búsqueda Binaria"] = fin-inicio
    else:
        print(f"\n'{busqueda}' no se encontró exactamente")
        print(f"Tiempo de Búsqueda Binaria: {tiempos_ef["Búsqueda Binaria"]}")
        print("Buscando coincidencias similares.\n")
        encontrados = []
        inicio = time.time()
        for titulo in valores_ef:
            if horspool_search_Main(titulo, busqueda) != -1:
                encontrados.append(titulo)
        fin = time.time()
        tiempos_ef["Horspool"] = fin - inicio

        if encontrados:
            print("Se han encontrado las siguientes coincidencias:\n")
            for e in encontrados:
                print(" -", e)
        else:
            print("No se encontraron coincidencias similares.")
        print(f"\nTiempo total de búsqueda con Horspool: {tiempos_ef["Horspool"]} segundos\n")

print("\nGenerando gráficas de comparación...")

plt.style.use("dark_background")
fig, ax = plt.subplots(1, 3, figsize=(18, 6))

alg1 = ["Bubble Sort", "Merge Sort"]
t1 = [tiempos_inef.get("Bubble Sort", 0.0), tiempos_ef.get("Merge Sort", 0.0)]
x1 = np.arange(len(alg1))
ax[0].plot(x1, t1, marker="o", linewidth=2)
ax[0].set_xticks(x1)
ax[0].set_xticklabels(alg1, rotation=15)
ax[0].set_title("Ordenamientos")
ax[0].set_ylabel("Tiempo (segundos)")
ax[0].grid(True, linestyle="--", alpha=0.3)

alg2 = ["Búsqueda Lineal", "Búsqueda Binaria"]
t2 = [tiempos_inef.get("Búsqueda Lineal", 0.0), tiempos_ef.get("Búsqueda Binaria", 0.0)]
x2 = np.arange(len(alg2))
ax[1].plot(x2, t2, marker="o", linewidth=2)
ax[1].set_xticks(x2)
ax[1].set_xticklabels(alg2, rotation=15)
ax[1].set_title("Búsqueda Exacta")
ax[1].set_ylabel("Tiempo (segundos)")
ax[1].grid(True, linestyle="--", alpha=0.3)

alg3 = ["Naive Search", "Horspool"]
t3 = [tiempos_inef.get("Naive Search", 0.0), tiempos_ef.get("Horspool", 0.0)]
x3 = np.arange(len(alg3))
ax[2].plot(x3, t3, marker="o", linewidth=2)
ax[2].set_xticks(x3)
ax[2].set_xticklabels(alg3, rotation=15)
ax[2].set_title("Búsqueda por similitud")
ax[2].set_ylabel("Tiempo (segundos)")
ax[2].grid(True, linestyle="--", alpha=0.3)

plt.tight_layout()
plt.show()
