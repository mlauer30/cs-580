# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
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
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
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
    "*** YOUR CODE HERE ***"
    stack=util.Stack()
    visited=[]
    startNode=(problem.getStartState(),[])        
    stack.push(startNode)
    while not stack.isEmpty():
        popped=stack.pop()
        location=popped[0]
        path=popped[1]
        if location not in visited:               
            visited.append(location)              
            if problem.isGoalState(location):
                return path
            successors=problem.getSuccessors(location)
            for successor in list(successors):
                if successor[0] not in visited:
                    stack.push((successor[0],path+[successor[1]]))
    return []    
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    queue=util.Queue()
    visited=[]                                                       
    startNode=(problem.getStartState(),[])                           
    queue.push(startNode)
    while not queue.isEmpty():
        popped=queue.pop()
        location=popped[0]
        path=popped[1]
        if location not in visited:
            visited.append(location)
            if problem.isGoalState(location):
                return path
            successors=problem.getSuccessors(location)
            for successor in list(successors):
                if successor[0] not in visited:
                    queue.push((successor[0],path + [successor[1]]))
    return []
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    priority_queue=util.PriorityQueue()
    visited=dict()
    state=problem.getStartState()
    node = {}
    node["predecessor"]=None                                                             
    node["action"]=None                                                              
    node["state"]=state
    node["cost"]=0
    priority_queue.push(node,node["cost"])

    while not priority_queue.isEmpty():
        node=priority_queue.pop()
        state=node["state"]
        cost=node["cost"]

        if state in visited:
            continue
        visited[state]=True
        if problem.isGoalState(state)==True:
            break
        for successor in problem.getSuccessors(state):
            if not successor[0] in visited:
                new_node={}
                new_node["predecessor"]=node
                new_node["state"]=successor[0]
                new_node["action"]=successor[1]
                new_node["cost"]=successor[2]+cost
                priority_queue.push(new_node,new_node["cost"])
    actions=[]
    while node["action"] !=None:
        actions.insert(0,node["action"])
        node=node["predecessor"]
    return actions
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    priority_queue=util.PriorityQueue()
    visited=dict()

    state=problem.getStartState()
    node={}
    node["predecessor"]=None
    node["action"]=None
    node["state"]=state
    node["cost"]=0
    node["total_cost_estimate"]=heuristic(state,problem)
    priority_queue.push(node,node["cost"]+node["total_cost_estimate"])

    while not priority_queue.isEmpty():
        node=priority_queue.pop()
        state=node["state"]
        cost=node["cost"]
                                                                        
        if state in visited:                                              
            continue
        visited[state]=True
        if problem.isGoalState(state)==True:
            break
        for successor in problem.getSuccessors(state):
            if not successor[0] in visited:
                new_node={}
                new_node["predecessor"]=node
                new_node["state"]=successor[0]
                new_node["action"]=successor[1]
                new_node["cost"]=successor[2] + cost
                new_node["total_cost_estimate"]=heuristic(new_node["state"],problem)
                priority_queue.push(new_node,new_node["cost"]+new_node["total_cost_estimate"])
    actions= []
    while node["action"]!=None:
        actions.insert(0,node["action"])
        node=node["predecessor"]
    return actions
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
