"""Week 12: Monster Hunter Graphs.

Complete each function using Python 3.11+.

Rules:
- Standard library only.
- Use type hints.
- Keep public function docstrings.
- Run tests with: pytest -q
"""

import heapq


def build_hunter_map(edges: list[tuple[str, str]]) -> dict[str, list[str]]:
    """Build an undirected adjacency list from route pairs."""

    graph: dict[str, list[str]] = {}

    for start, end in edges:

        if start not in graph:
            graph[start] = []

        if end not in graph:
            graph[end] = []

        if end not in graph[start]:
            graph[start].append(end)

        if start not in graph[end]:
            graph[end].append(start)

    return graph


def build_weighted_hunter_map(
    edges: list[tuple[str, str, int]]
) -> dict[str, dict[str, int]]:
    """Build an undirected weighted graph from route triples."""

    graph: dict[str, dict[str, int]] = {}

    for start, end, weight in edges:

        if weight <= 0:
            raise ValueError("Danger scores must be positive integers.")

        if start not in graph:
            graph[start] = {}

        if end not in graph:
            graph[end] = {}

        # Keep smallest weight if duplicate route exists
        if end not in graph[start] or weight < graph[start][end]:
            graph[start][end] = weight
            graph[end][start] = weight

    return graph


def map_summary(graph: dict[str, list[str]]) -> dict[str, int]:
    """Return the number of locations and undirected routes."""

    locations = len(graph)

    total_edges = 0

    for neighbors in graph.values():
        total_edges += len(neighbors)

    routes = total_edges // 2

    return {
        "locations": locations,
        "routes": routes,
    }


def most_connected_location(graph: dict[str, list[str]]) -> str | None:
    """Return the location with the most neighbors."""

    if not graph:
        return None

    best_location = None
    max_connections = -1

    for location in sorted(graph.keys()):

        connections = len(graph[location])

        if connections > max_connections:
            max_connections = connections
            best_location = location

    return best_location


def priority_hunt_order(reports: list[tuple[int, str]]) -> list[str]:
    """Return monster sighting locations from most urgent to least urgent."""

    heap = []

    for priority, location in reports:
        heapq.heappush(heap, (priority, location))

    result = []

    while heap:
        _, location = heapq.heappop(heap)
        result.append(location)

    return result