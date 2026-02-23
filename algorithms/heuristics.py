import math
from typing import Any, Tuple
from algorithms import utils
from algorithms.problems import MultiSurvivorProblem


def _manhattan_distance(p1, p2):
    """Calcula distancia Manhattan entre dos puntos."""
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def manhattanHeuristic(state, problem):
    """
    The Manhattan distance heuristic.
    """
    objetivo = problem.goal
    return _manhattan_distance(state, objetivo)


def euclideanHeuristic(state, problem):
    """
    The Euclidean distance heuristic.
    """
    # TODO: Add your code here
    objetivo = problem.goal
    distancia_euclideana = math.sqrt((state[0]+objetivo[0])^2 + (state[1]+objetivo[1])^2)
    return distancia_euclideana

def survivorHeuristic(state: Tuple[Tuple, Any], problem: MultiSurvivorProblem):
    """
    Your heuristic for the MultiSurvivorProblem.

    state: (position, survivors_grid)
    problem: MultiSurvivorProblem instance

    This must be admissible and preferably consistent.

    Hints:
    - Use problem.heuristicInfo to cache expensive computations
    - Go with some simple heuristics first, then build up to more complex ones
    - Consider: distance to nearest survivor + MST of remaining survivors
    - Balance heuristic strength vs. computation time (do experiments!)
    """
    position, survivors_grid = state
    survivors = get_survivor_positions(survivors_grid)
    if not survivors:
        return 0
    min_dist = min(
        abs(position[0] - s[0]) + abs(position[1] - s[1])
        for s in survivors
    )
    key = tuple(sorted(survivors))
    if key not in problem.heuristicInfo:
        problem.heuristicInfo[key] = mst_cost(survivors)
    mst = problem.heuristicInfo[key]
    return min_dist + mst
    

def mst_cost(points):
    """
    Computes the MST cost of a set of points using Manhattan distance.
    
    points: list of (x, y)
    return: total MST cost
    """
    if not points:
        return 0
    visited = set()
    visited.add(points[0])
    distances = {}
    for p in points[1:]:
        distances[p] = abs(points[0][0] - p[0]) + abs(points[0][1] - p[1])
    total_cost = 0
    while len(visited) < len(points):
        closest_point = min(distances, key=distances.get)
        min_dist = distances[closest_point]
        total_cost += min_dist
        visited.add(closest_point)
        del distances[closest_point]
        for p in distances:
            new_dist = abs(closest_point[0] - p[0]) + abs(closest_point[1] - p[1])
            if new_dist < distances[p]:
                distances[p] = new_dist
    return total_cost

def get_survivor_positions(survivors_grid):
    positions = []
    for x in range(survivors_grid.width):
        for y in range(survivors_grid.height):
            if survivors_grid[x][y]:
                positions.append((x, y))
    return positions