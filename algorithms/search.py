from algorithms.problems import SearchProblem
import algorithms.utils as utils
from world.game import Directions
from algorithms.heuristics import nullHeuristic


def tinyHouseSearch(problem: SearchProblem):
    """
    Returns a sequence of moves that solves tinyHouse. For any other building, the
    sequence of moves will be incorrect, so only use this for tinyHouse.
    """
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    stack = utils.Stack()
    visited = set()
    nodo_ini = problem.getStartState()
    stack.push((nodo_ini, []))
    print(nodo_ini,'Nodo ini nig')
    while not stack.isEmpty():
        state =  stack.pop()
        vecinos = problem.getSuccessors(state[0])
        if (problem.isGoalState(state[0])):
            
            return state[1]
        else:
            for veci in vecinos:
                new_path = state[1] + [veci[1]]
                if(veci not in visited):
                    visited.add(veci)
                    stack.push((veci[0], new_path))
                    
    return []
    
 #   utils.raiseNotDefined()


def breadthFirstSearch(problem: SearchProblem):
    """
    Search the shallowest nodes in the search tree first.
    """
    # TODO: Add your code here
    queue = utils.Queue()
    node_ini = problem.getStartState()
    visited = set()
    queue.push((node_ini, []))
    while not queue.isEmpty():
        state = queue.pop()
        if (problem.isGoalState(state[0])):
            return state[1]
        if(state[0] not in visited):
            visited.add(state[0])
            vecinos = problem.getSuccessors(state[0])
            print("esto es un vecino nigg", vecinos)
            for veci in vecinos:
                new_path = state[1] + [veci[1]]
                queue.push((veci[0], new_path))
    return []
            
            
        
 


def uniformCostSearch(problem: SearchProblem):
    """
    Search the node of least total cost first.
    """

    # TODO: Add your code here
    utils.raiseNotDefined()


def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """
    Search the node that has the lowest combined cost and heuristic first.
    """
    # TODO: Add your code here
    utils.raiseNotDefined()


# Abbreviations (you can use them for the -f option in main.py)
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
