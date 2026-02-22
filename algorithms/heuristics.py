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
    survivors = survivors_grid.asList()
    
    if not survivors:
        return 0

    # Distancia Manhattan al sobreviviente más cercano osea p1 a p2 
    for s in survivors:
        dist = _manhattan_distance(position, s)
        if dist < float("inf"):
            nearest = dist

    # 2) MST 
    visited = set()
    mst_cost = 0
    pq = utils.PriorityQueue()
    
    start = survivors[0]
    visited.add(start)
    
    initial_nodes = []
    for node in survivors:
        if node != start:
            initial_nodes.append(node)
    
    for node in initial_nodes:
        dist = _manhattan_distance(start, node)
        pq.push((start, node), dist)
    
    # Prim 
    while len(visited) < len(survivors):
        from_node, to_node = pq.pop()
        
        if to_node not in visited:
            # Agregar arista al MST
            dist = _manhattan_distance(from_node, to_node)
            mst_cost += dist
            
            visited.add(to_node)
   
            unvisited_nodes = []
            for node in survivors:
                if node not in visited:
                    unvisited_nodes.append(node)
            
            for node in unvisited_nodes:
                dist = _manhattan_distance(to_node, node)
                pq.push((to_node, node), dist)
    
    return nearest + mst_cost
