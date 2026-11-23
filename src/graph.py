import json
import math
from pathlib import Path
from collections import defaultdict
import matplotlib.pyplot as plt
def haversine(lat1, lon1, lat2, lon2):
    earth_radius = 6371000
    lat1 = math.radians(lat1)
    lat2 = math.radians(lat2)
    delta_lat = math.radians(lat2 - lat1)
    delta_lon = math.radians(lon2 - lon1)
    a = (
        math.sin(delta_lat / 2) ** 2
        + math.cos(lat1) * math.cos(lat2)
        * math.sin(delta_lon / 2) ** 2
    )
    return 2 * earth_radius * math.atan2(
        math.sqrt(a),
        math.sqrt(1 - a)
    )
def coordinate_key(lon, lat):
    return (round(lat, 6), round(lon, 6))
def load_geojson_graph(filepath=None):
    if filepath is None:
        project_dir = Path(__file__).resolve().parent.parent
        filepath = project_dir / "data" / "tagamoa.geojson"
    with open(filepath, "r", encoding="utf-8") as file:
        data = json.load(file)
    roads = []
    connections = defaultdict(set)
    roads_at_point = defaultdict(set)
    for road_id, feature in enumerate(data["features"]):
        geometry = feature.get("geometry")
        if not geometry or geometry["type"] != "LineString":
            continue
        coordinates = geometry["coordinates"]
        if len(coordinates) < 2:
            continue
        properties = feature.get("properties") or {}
        road_name = (
            properties.get("name:en")
            or properties.get("name")
            or "Unnamed Street"
        )
        one_way = properties.get("oneway", "no")
        road = {
            "id": road_id,
            "coordinates": coordinates,
            "name": road_name,
            "oneway": one_way
        }
        roads.append(road)
        for lon, lat in coordinates:
            point = coordinate_key(lon, lat)
            roads_at_point[point].add(road_id)
        for i in range(len(coordinates) - 1):
            lon1, lat1 = coordinates[i]
            lon2, lat2 = coordinates[i + 1]
            point1 = coordinate_key(lon1, lat1)
            point2 = coordinate_key(lon2, lat2)
            if point1 == point2:
                continue
            connections[point1].add(point2)
            connections[point2].add(point1)
    junctions = set()
    for point, neighbors in connections.items():
        connection_count = len(neighbors)
        road_count = len(roads_at_point[point])
        if connection_count != 2 or road_count > 1:
            junctions.add(point)
    nodes = sorted(junctions)
    coord_to_id = {
        point: node_id
        for node_id, point in enumerate(nodes)
    }
    id_to_coord = {
        node_id: point
        for node_id, point in enumerate(nodes)
    }
    graph = defaultdict(list)
    segment_id = 0
    for road in roads:
        coordinates = road["coordinates"]
        junction_indices = []
        for i, (lon, lat) in enumerate(coordinates):
            point = coordinate_key(lon, lat)
            if point in coord_to_id:
                junction_indices.append(i)
        for i in range(len(junction_indices) - 1):
            start = junction_indices[i]
            end = junction_indices[i + 1]
            road_section = coordinates[start:end + 1]
            if len(road_section) < 2:
                continue
            start_lon, start_lat = road_section[0]
            end_lon, end_lat = road_section[-1]
            start_point = coordinate_key(start_lon, start_lat)
            end_point = coordinate_key(end_lon, end_lat)
            u = coord_to_id[start_point]
            v = coord_to_id[end_point]
            if u == v:
                continue
            distance = 0
            for j in range(len(road_section) - 1):
                lon1, lat1 = road_section[j]
                lon2, lat2 = road_section[j + 1]
                distance += haversine(
                    lat1, lon1, lat2, lon2
                )
            geometry = [
                (lat, lon)
                for lon, lat in road_section
            ]
            edge = (
                v,
                round(distance, 2),
                road["name"],
                geometry,
                segment_id
            )
            if road["oneway"] == "-1":
                reverse_geometry = list(reversed(geometry))
                graph[v].append((
                    u,
                    round(distance, 2),
                    road["name"],
                    reverse_geometry,
                    segment_id
                ))
            else:
                graph[u].append(edge)
                if road["oneway"] not in ("yes", "1", "true"):
                    graph[v].append((
                        u,
                        round(distance, 2),
                        road["name"],
                        list(reversed(geometry)),
                        segment_id
                    ))
            segment_id += 1
    return id_to_coord, graph

def plot_graph(nodes, graph):
    plt.figure(figsize=(12, 10))
    drawn_segments = set()
    for neighbors in graph.values():
        for v, distance, name, geometry, sid in neighbors:
            if sid in drawn_segments:
                continue
            drawn_segments.add(sid)
            latitudes = [point[0] for point in geometry]
            longitudes = [point[1] for point in geometry]
            plt.plot(
                longitudes,
                latitudes,
                color="#2563eb",
                linewidth=1
            )

    latitudes = [point[0] for point in nodes.values()]
    longitudes = [point[1] for point in nodes.values()]
    plt.scatter(
        longitudes,
        latitudes,
        color="red",
        s=18,
        zorder=5
    )
    plt.title("Tagamoa Road Network")
    plt.axis("equal")
    plt.axis("off")
    plt.tight_layout()
    plt.show()
if __name__ == "__main__":
    nodes, graph = load_geojson_graph()
    directed_edges = sum(
        len(neighbors)
        for neighbors in graph.values()
    )
    print("Nodes:", len(nodes))
    print("Directed edges:", directed_edges)
    plot_graph(nodes, graph)
