from src.graph import load_geojson_graph
nodes, graph = load_geojson_graph("data/tagamoa.geojson")
print(f"Total Nodes: {len(nodes)}")
print(f"Total Vertices: {len(graph)}")
street_names = set()
for neighbors in graph.values():
    for _, _, street_name, _, _ in neighbors:
        street_names.add(street_name)
print(f"\nTotal Unique Streets: {len(street_names)}")
print("-" * 40)
for name in sorted(street_names):
    print(name)