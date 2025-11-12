import pandas as pd
import time
from sandbox_editado import merge_sort, busqueda_binaria_main, horspool_search_Main
import matplotlib.pyplot as plt

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
    plt.figure(figsize=(8, 5))
    plt.bar(tiempos.keys(), tiempos.values(), color=['#64B5F6', '#4DB6AC', '#AED581'])
    plt.title("Comparación de tiempos - Algoritmos Eficientes")
    plt.ylabel("Tiempo (segundos)")
    plt.xlabel("Algoritmo")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()
