from collections import defaultdict
import itertools
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt


def load_dataset(path="dataset.xlsx"):
    """Carga un Excel/CSV si existe; devuelve DataFrame."""
    try:
        if str(path).lower().endswith(".csv"):
            return pd.read_csv(path)
        return pd.read_excel(path)
    except Exception as e:
        raise RuntimeError(f"No se pudo leer '{path}': {e}")


def detect_user_and_item_columns(df):
    """Detecta columnas típicas para usuario/item. Devuelve (user_col, item_col)."""
    cols = [c.lower() for c in df.columns]
    user_candidates = [c for c in df.columns if c.lower() in ("user", "user_id", "userid", "customer", "client")]
    item_candidates = [c for c in df.columns if c.lower() in ("title", "movie", "item", "product", "name")]
    user_col = user_candidates[0] if user_candidates else None
    item_col = item_candidates[0] if item_candidates else None
    return user_col, item_col


def build_cooccurrence_graph(df, user_col=None, item_col=None, chunk_size=5, min_edge_weight=1):
    """
    Construye un grafo no dirigido donde nodos = items y aristas indican co-ocurrencia
    en las preferencias de un mismo usuario. Si no se detecta user_col, se crean
    'pseudo-usuarios' agrupando el dataset en chunks de tamaño chunk_size.
    """
    if item_col is None:
        raise ValueError("Se requiere item_col para construir el grafo.")
    G = nx.Graph()

    # preparar listas por usuario
    if user_col and user_col in df.columns:
        groups = df.groupby(user_col)[item_col].apply(list)
        user_lists = [list(map(str, lst)) for lst in groups]
    else:
        # crear pseudo-usuarios por bloques
        items = list(map(str, df[item_col].tolist()))
        user_lists = [items[i:i + chunk_size] for i in range(0, len(items), chunk_size)]

    edge_weights = defaultdict(int)
    for items in user_lists:
        unique_items = list(dict.fromkeys(items))  # mantener orden pero quitar duplicados
        for a, b in itertools.combinations(unique_items, 2):
            if a == b:
                continue
            key = tuple(sorted((a, b)))
            edge_weights[key] += 1

    # añadir nodos y aristas con peso
    for (a, b), w in edge_weights.items():
        if w >= min_edge_weight:
            G.add_node(a)
            G.add_node(b)
            G.add_edge(a, b, weight=w)

    # Añadir nodos aislados (por si existen items sin co-ocurrencias)
    for itm in df[item_col].astype(str).unique():
        if itm not in G:
            G.add_node(itm)

    return G


def top_items_by_weighted_degree(G, top_n=10):
    """Devuelve lista (item, weighted_degree) ordenada desc."""
    weighted_degrees = {n: sum(d.get("weight", 1) for _, _, d in G.edges(n, data=True)) for n in G.nodes()}
    return sorted(weighted_degrees.items(), key=lambda x: x[1], reverse=True)[:top_n]


def visualize_preference_subgraph(G, top_n=30, figsize=(12, 9), save_path="preference_graph.png"):
    """
    Visualiza un subgrafo formado por los top_n items por grado ponderado.
    Guarda imagen y muestra la ventana.
    """
    top_nodes = [n for n, _ in top_items_by_weighted_degree(G, top_n)]
    subG = G.subgraph(top_nodes).copy()

    # calcular tamaños y etiquetas
    weighted_deg = {n: sum(d.get("weight", 1) for _, _, d in subG.edges(n, data=True)) for n in subG.nodes()}
    max_w = max(weighted_deg.values()) if weighted_deg else 1
    node_sizes = [300 + (weighted_deg.get(n, 0) / max_w) * 3000 for n in subG.nodes()]

    plt.figure(figsize=figsize)
    pos = nx.spring_layout(subG, seed=42, k=0.5)
    edges = subG.edges(data=True)
    weights = [d.get("weight", 1) for (_, _, d) in edges]

    nx.draw_networkx_nodes(subG, pos, node_size=node_sizes, node_color="C0", alpha=0.9)
    nx.draw_networkx_edges(subG, pos, width=[1 + w * 0.5 for w in weights], alpha=0.7)
    nx.draw_networkx_labels(subG, pos, font_size=9)
    plt.title(f"Subgrafo de preferencias — Top {len(subG.nodes())} items")
    plt.axis("off")
    plt.tight_layout()
    plt.savefig(save_path, dpi=150)
    plt.show()
    return save_path


def summary_metrics(G, top_n=10):
    top = top_items_by_weighted_degree(G, top_n)
    total_nodes = G.number_of_nodes()
    total_edges = G.number_of_edges()
    return {"total_nodes": total_nodes, "total_edges": total_edges, "top_items": top}