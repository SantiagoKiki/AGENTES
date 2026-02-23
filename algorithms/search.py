from algorithms.problems import SearchProblem
import algorithms.utils as utils
from world.game import Directions
from algorithms.heuristics import euclideanHeuristic, manhattanHeuristic, nullHeuristic, survivorHeuristic


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
    # TODO: Add your code here
    stack = utils.Stack()
    visited = set()
    start = problem.getStartState()

    stack.push((start, []))
    while not stack.isEmpty():
        state, path = stack.pop()

        if problem.isGoalState(state):
            return path
        
        if state not in visited:
            visited.add(state)

            for succesor, action, cost in problem.getSuccessors(state):
                new_path = path + [action]
                stack.push((succesor, new_path))
                
    # print(problem)
    utils.raiseNotDefined()
    return []
        



def breadthFirstSearch(problem: SearchProblem):
    """
    Search the shallowest nodes in the search tree first.
    """
    stack = utils.Queue()
    visited = set()
    start = problem.getStartState()

    stack.push((start, []))
    while not stack.isEmpty():
        state, path = stack.pop()

        if problem.isGoalState(state):
            return path
        
        if state not in visited:
            visited.add(state)

            for succesor, action, cost in problem.getSuccessors(state):
                new_path = path + [action]
                stack.push((succesor, new_path))
                
    # print(problem)
    utils.raiseNotDefined()
    return []
            
            
        

def uniformCostSearch(problem: SearchProblem):
    nodo_ini = problem.getStartState()
    prio_queue = utils.PriorityQueue()
    visitados = set()
    prio_queue.push((nodo_ini, []), 0)
    while not prio_queue.isEmpty():
        state = prio_queue.pop()
        if problem.isGoalState(state[0]):
            return state[1]
        if state[0] not in visitados:
            visitados.add(state[0])
            costo_acci = problem.getCostOfActions(state[1])
            vecinos = problem.getSuccessors(state[0])
            for veci in vecinos:
                new_path = state[1] + [veci[1]]

                costo = problem.getCostOfActions(new_path)
                prio_queue.push((veci[0], new_path), costo)


def aStarSearch(problem: SearchProblem, heuristic=manhattanHeuristic):
    """
    Search the node that has the lowest combined cost and heuristic first.
    """
    # TODO: Add your code here
    nodo_ini = problem.getStartState()
    prio_queue = utils.PriorityQueue()
    visitados = set()
    prio_queue.push((nodo_ini, []), 0)
    while not prio_queue.isEmpty():
        state = prio_queue.pop()
        if problem.isGoalState(state[0]):
            return state[1]
        if state[0] not in visitados:
            visitados.add(state[0])
            vecinos = problem.getSuccessors(state[0])
            for veci in vecinos:
                new_path = state[1] + [veci[1]]
                costo = problem.getCostOfActions(new_path)
                prio_queue.push((veci[0], new_path), costo+heuristic(state[0], problem))
            

    return []
            
            

# Abbreviations (you can use them for the -f option in main.py)
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
