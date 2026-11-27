import json
from pathlib import Path
from src.graph import load_geojson_graph


def export_processed_data(
    geojson_path="data/tagamoa.geojson",
    output_dir="data/processed",
):
    nodes, graph = load_geojson_graph(geojson_path)
    out_path = Path(output_dir)
    out_path.mkdir(parents=True, exist_ok=True)

    locations = []
    valid_ids = set()
    for node_id in sorted(nodes.keys()):
        lat, lon = nodes[node_id]
        locations.append({
            "id": node_id,
            "name": f"Intersection_{node_id}",
            "lat": lat,
            "lon": lon,
        })
        valid_ids.add(node_id)

    existing_roads = []
    seen_segments = set()
    invalid_roads = 0

    for u, neighbors in graph.items():
        for v, distance, street_name, _geometry, sid in neighbors:
            if u not in valid_ids or v not in valid_ids:
                invalid_roads += 1
                continue

            if sid in seen_segments:
                continue
            seen_segments.add(sid)

            existing_roads.append({
                "id": sid,
                "from": u,
                "to": v,
                "weight": distance,
                "name": street_name,
                "oneway": True,
            })

    locations_file = out_path / "locations.json"
    roads_file = out_path / "existing_roads.json"

    with open(locations_file, "w", encoding="utf-8") as f:
        json.dump(locations, f, indent=2, ensure_ascii=False)

    with open(roads_file, "w", encoding="utf-8") as f:
        json.dump(existing_roads, f, indent=2, ensure_ascii=False)

    print(f"Saved {len(locations)} locations -> {locations_file}")
    print(f"Saved {len(existing_roads)} roads -> {roads_file}")
    print(f"Invalid roads skipped: {invalid_roads}")


if __name__ == "__main__":
    export_processed_data()