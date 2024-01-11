import networkx as nx
import random
import matplotlib.pyplot as plt

# Número de nodos (empleados, tareas, etc.)
num_nodos = 5

# Crear un grafo dirigido ponderado
G = nx.DiGraph()

# Agregar nodos al grafo
nodos = [f"Nodo{i}" for i in range(num_nodos)]
G.add_nodes_from(nodos)

# Agregar arcos con capacidad y costo aleatorios al grafo
for i in range(num_nodos):
    for j in range(num_nodos):
        if i != j:  # Evitar bucles
            capacidad = random.randint(1, 20)  # Capacidad aleatoria entre 1 y 20
            costo = random.randint(1, 10)  # Costo aleatorio entre 1 y 10
            G.add_edge(f"Nodo{i}", f"Nodo{j}", capacity=capacidad, weight=costo)

# Resolver el Problema de Flujo Máximo
max_flow_value, flow_dict = nx.maximum_flow(G, f"Nodo0", f"Nodo{num_nodos-1}")

# Dibujar el grafo con capacidades de flujo y costos en los arcos
pos = nx.spring_layout(G)
nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=700,
    node_color="skyblue",
    font_size=10,
    font_color="black",
    font_weight="bold",
)

# Dibujar capacidades de flujo y costos en los arcos
labels_capacidades = nx.get_edge_attributes(G, "capacity")
labels_costos = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels_capacidades, font_color="red")
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels_costos, font_color="blue")

# Dibujar el flujo actual
edge_colors = [
    "red" if flow_dict[edge[0]][edge[1]] > 0 else "black" for edge in G.edges()
]
nx.draw(G, pos, edge_color=edge_colors, width=2)

plt.show()
