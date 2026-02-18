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
        print("Esto es un estado",state)

        if (problem.isGoalState(state[0])):
            return state[1]
        if(state[0] not in visited):
            visited.add(state[0])
            vecinos = problem.getSuccessors(state[0])
            for veci in vecinos:
                new_path = state[1] + [veci[1]]
                queue.push((veci[0], new_path))
    return []
            
            
        
 


# def uniformCostSearch(problem: SearchProblem):
#     """
#     Search the node of least total cost first.
#     """
#     prio_queue = utils.PriorityQueue()
#     valor = 0
#     visitados = set()
#     rutica =    []
#     state = problem.getStartState()
#     while not prio_queue.isEmpty() or valor != 1:
#         print("Esto es un state 0", state)
#         if valor == 0:
#             prio_queue.push((state, []), 0)
#             state = ((state, []), 0)
#             print("Estado ele o ele", state)
#             vecinos = problem.getSuccessors(state[0][0])
#             valor +=1
#         else:
#             print("Else", state[0])
#             vecinos = problem.getSuccessors(state)

#         print("Esto es un estado", state)
#         print(vecinos)
        
#         for veci in vecinos:
#             print("Esto es uin vecino: ", veci)
#             if(problem.isGoalState(veci[0])):
#                 return rutica
#             if(veci not in visitados):
#                 visitados.add(veci[0])
#                 print("Esto es un vecino :)", veci)
#                 newpath = rutica + [veci[1]]
#         prio_queue.push((veci[0], newpath),veci[2])
#         state, rutica = prio_queue.pop()


   
    # TODO: Add your code here


def uniformCostSearch(problem: SearchProblem):
    nodo_ini = problem.getStartState()
    prio_queue = utils.PriorityQueue()
    visitados = set()
    prio_queue.push((nodo_ini, []), 0)
    while not prio_queue.isEmpty():
        state = prio_queue.pop()
        print(state)
        if problem.isGoalState(state[0]):
            return state[1]
        if state[0] not in visitados:
            visitados.add(state[0])
            costo_acci = problem.getCostOfActions(state[1])
            vecinos = problem.getSuccessors(state[0])
            for veci in vecinos:
                new_path = state[1] + [veci[1]]
                print(veci, "Eso es un veci")
                print(veci[1], "Eso es un veci 1")
                print(veci[0], "Eso es un veci 0")
                prio_queue.push((veci[0], new_path), new_path)


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
