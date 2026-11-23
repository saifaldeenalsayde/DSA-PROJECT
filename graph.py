import json
import math
from collections import defaultdict
import matplotlib.pyplot as plt

def haversine(lat1, lon1, lat2, lon2):
    R = 6371000
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)
    a = math.sin(dphi / 2)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2)**2
    return 2 * R * math.atan2(math.sqrt(a), math.sqrt(1 - a))

def load_geojson_graph(filepath="tagamoa.geojson"):
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    coord_to_id = {}
    id_to_coord = {}
    graph = defaultdict(list)
    next_id = 0

    def get_node_id(lon, lat):
        nonlocal next_id
        key = (round(lat, 6), round(lon, 6))
        if key not in coord_to_id:
            coord_to_id[key] = next_id
            id_to_coord[next_id] = key
            next_id += 1
        return coord_to_id[key]

    for feature in data.get('features', []):
        geom = feature.get('geometry', {})
        props = feature.get('properties', {})

        if geom.get('type') == 'LineString':
            coords = geom.get('coordinates', [])
            # بياخد الاسم الإنجليزي الأساسي الأول، ولو مش موجود ياخد name (مش alt_name)
            street_name = props.get('name:en') or props.get('name') or 'Unnamed Street'
            is_oneway = props.get('oneway') == 'yes'

            for i in range(len(coords) - 1):
                lon1, lat1 = coords[i]
                lon2, lat2 = coords[i + 1]

                u = get_node_id(lon1, lat1)
                v = get_node_id(lon2, lat2)
                dist = round(haversine(lat1, lon1, lat2, lon2), 2)

                graph[u].append((v, dist, street_name))
                if not is_oneway:
                    graph[v].append((u, dist, street_name))

    return id_to_coord, graph

def plot_graph(nodes, graph, title="Tagamoa - Fifth Settlement"):
    plt.figure(figsize=(10, 8))

    xs, ys = [], []
    for u, neighbors in graph.items():
        lat1, lon1 = nodes[u]
        for v, _, _ in neighbors:
            lat2, lon2 = nodes[v]
            xs.extend([lon1, lon2, None])
            ys.extend([lat1, lat2, None])

    plt.plot(xs, ys, color='#2563eb', linewidth=1.2)

    lats = [coord[0] for coord in nodes.values()]
    lons = [coord[1] for coord in nodes.values()]
    plt.scatter(lons, lats, color='red', s=6, zorder=5)

    plt.title(title)
    plt.axis('equal')
    plt.axis('off')
    plt.show()

# الجزء ده هيشتغل بس لما تعمل Run لملف graph.py مباشرة
if __name__ == "__main__":
    nodes, graph = load_geojson_graph("tagamoa.geojson")
    plot_graph(nodes, graph)