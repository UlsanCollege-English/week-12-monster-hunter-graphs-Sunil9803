"""Week 12: Monster Hunter Graphs."""

import heapq


def build_hunter_map(edges: list[tuple[str, str]]) -> dict[str, list[str]]:
    graph = {}

    for a, b in edges:
        if a not in graph:
            graph[a] = []

        if b not in graph:
            graph[b] = []

        if b not in graph[a]:
            graph[a].append(b)

        if a not in graph[b]:
            graph[b].append(a)

    return graph


def build_weighted_hunter_map(
    edges: list[tuple[str, str, int]]
) -> dict[str, dict[str, int]]:

    graph = {}

    for a, b, weight in edges:

        if weight <= 0:
            raise ValueError("Danger score must be positive")

        if a not in graph:
            graph[a] = {}

        if b not in graph:
            graph[b] = {}

        if b not in graph[a] or weight < graph[a][b]:
            graph[a][b] = weight
            graph[b][a] = weight

    return graph


def map_summary(graph: dict[str, list[str]]) -> dict[str, int]:

    locations = len(graph)

    total_neighbors = 0

    for neighbors in graph.values():
        total_neighbors += len(neighbors)

    routes = total_neighbors // 2

    return {
        "locations": locations,
        "routes": routes,
    }


def most_connected_location(graph: dict[str, list[str]]) -> str | None:

    if not graph:
        return None

    best_location = None
    best_count = -1

    for location in sorted(graph.keys()):

        count = len(graph[location])

        if count > best_count:
            best_count = count
            best_location = location

    return best_location


def priority_hunt_order(reports: list[tuple[int, str]]) -> list[str]:

    heap = []

    for priority, location in reports:
        heapq.heappush(heap, (priority, location))

    result = []

    while heap:
        priority, location = heapq.heappop(heap)
        result.append(location)

    return result