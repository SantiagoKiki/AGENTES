from typing import Any, Tuple
from algorithms import utils
from algorithms.problems import MultiSurvivorProblem


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
    # TODO: Add your code here
    utils.raiseNotDefined()


def euclideanHeuristic(state, problem):
    """
    The Euclidean distance heuristic.
    """
    # TODO: Add your code here
    utils.raiseNotDefined()


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
    # TODO: Add your code here
    from typing import Any, Tuple
from algorithms import utils
from algorithms.problems import MultiSurvivorProblem
import math


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
    
    goal = problem.goal
    return abs(state[0] - goal[0]) + abs(state[1] - goal[1])
    utils.raiseNotDefined()


def euclideanHeuristic(state, problem):
    """
    The Euclidean distance heuristic.
    """
    goal = problem.goal  # o como esté definido en tu problema
    
    x1, y1 = state
    x2, y2 = goal
    
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    utils.raiseNotDefined()


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
    position, remaining = state
    
    if not remaining:
        return 0
    
    # Distancia al más cercano
    min_dist = min(
        abs(position[0] - s[0]) + abs(position[1] - s[1])
        for s in remaining
    )
    
    # Distancia máxima entre sobrevivientes
    max_pair_dist = 0
    for s1 in remaining:
        for s2 in remaining:
            dist = abs(s1[0] - s2[0]) + abs(s1[1] - s2[1])
            max_pair_dist = max(max_pair_dist, dist)
    
    return min_dist + max_pair_dist
    # TODO: Add your code here
    utils.raiseNotDefined()

    utils.raiseNotDefined()
