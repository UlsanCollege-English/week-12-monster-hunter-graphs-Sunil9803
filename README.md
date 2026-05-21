[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/80z-ZS6n)

# Week 12: Monster Hunter Graphs

## Student

Name: Sunil Khadka

Student ID: TODO

---

## Summary

This assignment builds and analyzes monster hunter graphs using adjacency lists and weighted graphs.  
The locations in the graph represent monster sighting areas, while the routes represent paths between those locations.  
The program creates both normal and weighted graphs, counts locations and routes, finds the most connected location, and orders monster hunt reports by urgency using a heap priority queue.  
The hardest function was building the weighted graph because duplicate routes had to keep only the lowest danger score.

---

## Approach

- `build_hunter_map`:
  - Created an empty dictionary for the graph.
  - Added both directions for each route because the graph is undirected.
  - Used membership checks to avoid duplicate neighbors.

- `build_weighted_hunter_map`:
  - Built a nested dictionary structure.
  - Added routes in both directions.
  - Checked for invalid weights and raised `ValueError` for zero or negative scores.
  - Kept the smallest danger score if duplicate routes appeared.

- `map_summary`:
  - Counted total locations using `len(graph)`.
  - Counted all neighbor connections and divided by 2 because routes are undirected.

- `most_connected_location`:
  - Compared neighbor counts for each location.
  - Used alphabetical order to break ties.

- `priority_hunt_order`:
  - Used `heapq` as a min-heap.
  - Pushed all reports into the heap.
  - Removed reports in priority order and stored the locations.

---

## Complexity

### `build_hunter_map`

- Time: `O(E)`
- Space: `O(V + E)`
- Why:
  - Each edge is processed once.
  - The graph stores all locations and routes.

### `build_weighted_hunter_map`

- Time: `O(E)`
- Space: `O(V + E)`
- Why:
  - Each weighted edge is checked and inserted once.
  - The nested dictionary stores all routes and weights.

### `map_summary`

- Time: `O(V + E)`
- Space: `O(1)`
- Why:
  - The function loops through every node and neighbor.
  - Only a few counters are used.

### `most_connected_location`

- Time: `O(V)`
- Space: `O(1)`
- Why:
  - Each location is checked once.
  - No extra data structure grows with input size.

### `priority_hunt_order`

- Time: `O(n log n)`
- Space: `O(n)`
- Why:
  - Heap insertion and removal both take `log n`.
  - The heap stores all reports.

---

## Edge-Case Checklist

- [x] Empty graph
- [x] One route
- [x] Duplicate routes
- [x] Disconnected locations
- [x] Tie for most connected location
- [x] Positive weighted routes
- [x] Invalid zero or negative danger score
- [x] Empty priority report list

---

## Tests

Paste the result of your test run.

```bash
pytest -q