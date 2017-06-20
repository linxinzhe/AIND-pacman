# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called 
by Pacman agents (in searchAgents.py).
"""

import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def solution(node):
    l = list()
    while True:
        l.append(node['action'])
        node = node["parent"]
        if not node:
            l.pop()
            break
    l.reverse()
    return l


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first
    [2nd Edition: p 75, 3rd Edition: p 87]

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm
    [2nd Edition: Fig. 3.18, 3rd Edition: Fig 3.7].

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"


def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    [2nd Edition: p 73, 3rd Edition: p 82]
    """
    "*** YOUR CODE HERE ***"
    node = {'state': problem.getStartState(),
            'action': None,
            'path_cost': 0,
            'parent': None}

    if problem.isGoalState(node['state']):
        return node['action']

    frontier = util.Queue()
    frontier.push(node)

    explored = set()

    while True:
        if frontier.isEmpty():
            return None

        node = frontier.pop()
        explored.add(node['state'])

        state = node['state']
        for successor, action, stepCost in problem.getSuccessors(state):
            child = {'state': successor,
                     'action': action,
                     'path_cost': node['path_cost'] + stepCost,
                     'parent': node}
            if successor not in explored or successor not in frontier.list:
                if problem.isGoalState(successor):
                    return solution(child)
                frontier.push(child)


def in_heap(item, priorityQueue):
    for priority, node in priorityQueue.heap:
        if item['state'] == node['state']:
            return True
    return False


def is_higher(item, priorityQueue):
    for priority, node in priorityQueue.heap:
        if item['state'] == node['state'] and node['path_cost'] > item['path_cost']:
            return True
    return False


def replace(item, priorityQueue):
    for priority, node in priorityQueue.heap:
        if item['state'] == node['state'] and node['path_cost'] > item['path_cost']:
            node['parent'] = item['parent']
            node['path_cost'] = item['path_cost']
    return None


def uniformCostSearch(problem):
    "Search the node of least total cost first. "
    "*** YOUR CODE HERE ***"
    node = {'state': problem.getStartState(),
            'action': None,
            'path_cost': 0,
            'parent': None}

    frontier = util.PriorityQueue()
    frontier.push(node, node['path_cost'])

    explored = set()

    while True:
        if frontier.isEmpty():
            return None

        node = frontier.pop()

        if problem.isGoalState(node['state']):
            return solution(node)

        state = node['state']
        explored.add(state)

        for successor, action, stepCost in problem.getSuccessors(state):
            child = {'state': successor,
                     'action': action,
                     'path_cost': node['path_cost'] + stepCost,
                     'parent': node}
            if successor not in explored or not in_heap(child, frontier):
                frontier.push(child, stepCost)
            elif is_higher(child, frontier):
                replace(child, frontier)


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
