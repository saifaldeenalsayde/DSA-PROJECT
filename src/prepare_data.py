import json
from pathlib import Path
from graph import get_distance, load_geojson_graph

#generate candidate_roads.json
cost_per_meter = 3000
def build_candidate_roads(
    locations,
):
    candidate_roads = []
    road_id = 0

    for i in range(len(locations)):
        for j in range(i + 1, len(locations)):
            loc1 = locations[i]
            loc2 = locations[j]
            dist = get_distance(loc1["lat"], loc1["lon"], loc2["lat"], loc2["lon"])

            if 50 <= dist <= 300:
                cost = round(dist * cost_per_meter, 2)
                candidate_roads.append({
                    "road_id": road_id,
                    "u": loc1["id"],
                    "v": loc2["id"],
                    "distance_m": round(dist, 2),
                    "cost": cost,
                })
                road_id += 1

    return {
        "metadata": {
            "data_type": "simulated_candidate_roads",
            "cost_assumption": f"distance_meters * {int(cost_per_meter)} EGP/meter",
            "distance_range_m": [50, 300],
        },
        "roads": candidate_roads,
    }

def export_processed_data(
    geojson_path="data/raw/tagamoa.geojson",
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

    candidate_payload = build_candidate_roads(locations)

    locations_file = out_path / "locations.json"
    roads_file = out_path / "existing_roads.json"
    candidates_file = out_path / "candidate_roads.json"

    with open(locations_file, "w", encoding="utf-8") as f:
        json.dump(locations, f, indent=2, ensure_ascii=False)

    with open(roads_file, "w", encoding="utf-8") as f:
        json.dump(existing_roads, f, indent=2, ensure_ascii=False)

    with open(candidates_file, "w", encoding="utf-8") as f:
        json.dump(candidate_payload, f, indent=2, ensure_ascii=False)

    print(f"Saved {len(locations)} locations -> {locations_file}")
    print(f"Saved {len(existing_roads)} roads -> {roads_file}")
    print(f"Saved {len(candidate_payload['roads'])} candidate roads -> {candidates_file}")
    print(f"Invalid roads skipped: {invalid_roads}")


if __name__ == "__main__":
    export_processed_data()
