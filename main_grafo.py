from grafo import *

if __name__ == "__main__":
    # Ejecución demo: intenta detectar columnas y genera salida medible + gráfico.
    df = load_dataset("dataset.xlsx")
    user_col, item_col = detect_user_and_item_columns(df)
    if not item_col:
        raise SystemExit("No se pudo detectar columna de items (intente renombrar a 'title' o 'movie').")

    print(f"Usando columnas -> usuario: {user_col}, item: {item_col}")
    G = build_cooccurrence_graph(df, user_col=user_col, item_col=item_col, chunk_size=5, min_edge_weight=1)
    metrics = summary_metrics(G, top_n=30)
    print(f"Total nodos: {metrics['total_nodes']}, aristas: {metrics['total_edges']}")
    print("Top 10 items por preferencia (grado ponderado):")
    for item, score in metrics["top_items"]:
        print(f" - {item} (score={score})")

    img = visualize_preference_subgraph(G, top_n=30, save_path="preference_graph.png")
    print(f"Gráfico guardado en: {img}")