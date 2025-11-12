import pandas as pd
import time
from sandbox import merge_sort, busqueda_binaria_main, horspool_search_Main
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_excel("dataset.xlsx")
valores = df['title'].astype(str).str.lower().tolist()[:1000]


print("Algoritmos eficientes")

tiempos = {}

inicio = time.time()
valores = merge_sort(valores)
fin = time.time()
tiempos['Merge Sort'] = fin - inicio
print(f"Merge Sort completado en: {fin - inicio:.4f} segundos")

while True:
    busqueda = input("Ingrese el título o parte del título que desea buscar, o toque enter para salir: ").strip()
    if not busqueda:
        print("\nPrograma finalizado.")
        break

    inicio = time.time()
    indice = busqueda_binaria_main(valores, busqueda)
    fin = time.time()
    tiempos['Búsqueda Binaria'] = fin - inicio

    if indice != -1:
        print(f"\nCoincidencia exacta encontrada:")
        print(f" {valores[indice]}")
        print(f"Tiempo de búsqueda: {fin - inicio:.6f} segundos\n")
    else:
        print(f"\n'{busqueda}' no se encontró exactamente. Buscando coincidencias similares.\n")
        encontrados = []
        pattern = busqueda.lower()
        inicio = time.time()
        for titulo in valores:
            texto = titulo.lower()
            if horspool_search_Main(texto, pattern) != -1:
                encontrados.append(titulo)
        fin = time.time()
        tiempos['Horspool'] = fin - inicio

        if encontrados:
            print("Se han encontrado las siguientes coincidencias:\n")
            for e in encontrados:
                print(" -", e)
        else:
            print("No se encontraron coincidencias similares.")
        print(f"\nTiempo total de búsqueda: {fin - inicio:.6f} segundos\n")

if tiempos:
    keys = list(tiempos.keys())
    values = list(tiempos.values())

    x = np.arange(len(keys))

    plt.style.use('dark_background')
    plt.figure(figsize=(10,6))

    plt.plot(x, values, color='red', marker='o', linewidth=2, label='Tiempos medidos')

    # Referencia lineal O(n)
    ref_linear = np.linspace(values[0], values[-1], len(values))
    plt.plot(x, ref_linear, linestyle='--', color='orange', label='Referencia O(n)')

    # Referencia logarítmica O(log n)
    ref_log = np.log2(np.arange(2, len(values)+2))
    ref_log = ref_log / ref_log.max() * max(values)
    plt.plot(x, ref_log, linestyle='--', color='blue', label='Referencia O(log n)')

    plt.xticks(x, keys, rotation=15)
    plt.xlabel("Algoritmo")
    plt.ylabel("Tiempo (segundos)")
    plt.title("Comparación de tiempos de ejecución")
    plt.grid(True, linestyle='--', alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.show()



