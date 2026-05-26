"""Week 12: Monster Hunter Graphs."""

from __future__ import annotations

import heapq


def build_hunter_map(edges: list[tuple[str, str]]) -> dict[str, list[str]]:
    """Build an undirected adjacency list from route pairs."""

    graph: dict[str, set[str]] = {}

    for a, b in edges:

        if a not in graph:
            graph[a] = set()

        if b not in graph:
            graph[b] = set()

        graph[a].add(b)
        graph[b].add(a)

    result: dict[str, list[str]] = {}

    for location in graph:
        result[location] = sorted(graph[location])

    return result


def build_weighted_hunter_map(
    edges: list[tuple[str, str, int]]
) -> dict[str, dict[str, int]]:
    """Build an undirected weighted graph from route triples."""

    graph: dict[str, dict[str, int]] = {}

    for a, b, weight in edges:

        if weight <= 0:
            raise ValueError("Danger score must be positive")

        if a not in graph:
            graph[a] = {}

        if b not in graph:
            graph[b] = {}

        if b not in graph[a]:
            graph[a][b] = weight
            graph[b][a] = weight

        else:
            current = graph[a][b]

            if weight < current:
                graph[a][b] = weight
                graph[b][a] = weight

    return graph


def map_summary(graph: dict[str, list[str]]) -> dict[str, int]:
    """Return the number of locations and undirected routes."""

    locations = len(graph)

    total = 0

    for neighbors in graph.values():
        total += len(neighbors)

    routes = total // 2

    return {
        "locations": locations,
        "routes": routes,
    }


def most_connected_location(graph: dict[str, list[str]]) -> str | None:
    """Return the location with the most neighbors."""

    if not graph:
        return None

    best_location = None
    best_count = -1

    for location in sorted(graph):

        count = len(graph[location])

        if count > best_count:
            best_count = count
            best_location = location

    return best_location


def priority_hunt_order(reports: list[tuple[int, str]]) -> list[str]:
    """Return monster sighting locations from most urgent to least urgent."""

    heap: list[tuple[int, str]] = []

    for priority, location in reports:
        heapq.heappush(heap, (priority, location))

    result: list[str] = []

    while heap:
        priority, location = heapq.heappop(heap)
        result.append(location)

    return result