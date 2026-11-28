import json
import math
from pathlib import Path


def haversine_m(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    r = 6371000.0
    p1, p2 = math.radians(lat1), math.radians(lat2)
    dp = math.radians(lat2 - lat1)
    dl = math.radians(lon2 - lon1)
    a = math.sin(dp / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 2 * r * math.atan2(math.sqrt(a), math.sqrt(1 - a))


def main(
    locations_path: str = "data/processed/locations.json",
    landmarks_path: str = "data/processed/landmarks.json",
) -> None:
    locations = json.loads(Path(locations_path).read_text(encoding="utf-8"))
    landmarks = json.loads(Path(landmarks_path).read_text(encoding="utf-8"))

    for place in landmarks:
        best_id = None
        best_dist = float("inf")
        for node in locations:
            dist = haversine_m(place["lat"], place["lon"], node["lat"], node["lon"])
            if dist < best_dist:
                best_dist = dist
                best_id = node["id"]
        place["nearest_node_id"] = best_id
        place["snap_distance_m"] = round(best_dist, 2)
        print(f"{place['name']} -> Node {best_id} ({place['snap_distance_m']} m)")

    Path(landmarks_path).write_text(
        json.dumps(landmarks, indent=2, ensure_ascii=False), encoding="utf-8"
    )


if __name__ == "__main__":
    main()