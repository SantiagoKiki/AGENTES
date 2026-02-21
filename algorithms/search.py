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
    utils.raiseNotDefined()


def uniformCostSearch(problem):
    nodoIni = problem.getStartState()

    prio_queue = utils.PriorityQueue() # cola de prioridad 

    visitados = set() # marco los nodos visitados para no ciclar

    prio_queue.push((nodoIni, []), 0) # inserto el nodo inicial con costo 0

    while not prio_queue.isEmpty(): # mientras la cola de prioridad no este vacia
        state = prio_queue.pop() # popeo el estado segun la cola de prioridad 

        #print(state) 
        if problem.isGoalState(state[0]): #Pregunto el caso base si si o en caso de que ya lo encontré con el pop

            return state[1] # devuelvo el camino
        if state[0] not in visitados: # si no está marcado 

            visitados.add(state[0]) # lo marco como visitado y lo proceso

            costo_acci = problem.getCostOfActions(state[1]) 

            vecinos = problem.getSuccessors(state[0]) # obtengo los vecinos del nodo actual
            for veci in vecinos: # para cada vecino del nodo actual

                new_path = state[1] + [veci[1]] # genero el nuevo camino a ese vecino 

                costo = problem.getCostOfActions(new_path) # calculo el costo del nuevo camino a ese vecino

                prio_queue.push((veci[0], new_path), costo) # lo meto en la cola de prioridad.
    return [] 

    # TODO: Add your code here
    utils.raiseNotDefined()



def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """
    Search the node that has the lowest combined cost and heuristic first.
    """
    frontier = utils.PriorityQueue()
    visited = set()

    start = problem.getStartState()
    frontier.push((start,[],0), heuristic(start, problem))
    while not frontier.isEmpty():
        state, path, cost =  frontier.pop()

        if problem.isGoalState(state):
            return path
        
        if state not in visited:
            visited.add(state)

            for succesor, action, stepCost in problem.getSuccessors(state):
                newCost = cost + stepCost
                newPath = path + [action]
                priority = newCost + heuristic(succesor,problem)
                frontier.push((succesor, newPath, newCost),priority)
        pass
    # TODO: Add your code here
    utils.raiseNotDefined()


# Abbreviations (you can use them for the -f option in main.py)
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
