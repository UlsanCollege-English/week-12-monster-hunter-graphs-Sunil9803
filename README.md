# Week 12: Monster Hunter Graphs

## Student

Name: Your Name

Student ID: Your Student ID

---

## Summary

This assignment builds graph helper functions for a monster hunter map system.  
The graph represents locations in the city where monster sightings have been reported.  
The routes between locations are stored using adjacency lists and weighted graphs.  
The program can summarize the graph, find the most connected location, and organize urgent monster reports using a priority queue with `heapq`.  
The hardest function was building the weighted graph because duplicate routes had to keep the lowest danger score.

---

## Approach

- `build_hunter_map`:
  - I created an adjacency list dictionary.
  - For each route, I added both directions because the graph is undirected.
  - I checked for duplicate neighbors before adding them.

- `build_weighted_hunter_map`:
  - I used nested dictionaries for weighted edges.
  - I added routes in both directions.
  - I raised `ValueError` for zero or negative weights.
  - If a duplicate route appeared, I kept the smaller danger score.

- `map_summary`:
  - I counted locations using the number of graph keys.
  - I counted all neighbors and divided by 2 because routes are undirected.

- `most_connected_location`:
  - I checked the number of neighbors for each location.
  - I tracked the largest connection count.
  - I used alphabetical order to break ties.

- `priority_hunt_order`:
  - I used `heapq` as a priority queue.
  - Lower priority numbers were removed first.
  - I stored the ordered locations in a result list.

---

## Complexity

### `build_hunter_map`

- Time: O(E)
- Space: O(V + E)
- Why:
  - Each edge is processed once and stored in the adjacency list.

### `build_weighted_hunter_map`

- Time: O(E)
- Space: O(V + E)
- Why:
  - Each weighted edge is processed once and stored in nested dictionaries.

### `map_summary`

- Time: O(V + E)
- Space: O(1)
- Why:
  - The function loops through all adjacency lists to count routes.

### `most_connected_location`

- Time: O(V)
- Space: O(1)
- Why:
  - Each location is checked once to compare neighbor counts.

### `priority_hunt_order`

- Time: O(N log N)
- Space: O(N)
- Why:
  - Heap insertion and removal each take logarithmic time.

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
```

Result:

```text
16 passed in 0.09s
```

---

## Assistance & Sources

AI used? Yes

If yes, what did it help with?

- Understanding graph logic
- Reviewing adjacency list structure
- Explaining complexity
- Debugging test failures

Other sources used:

- Class lecture notes
- Python documentation for `heapq`