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
from util import heappush, heappop
from collections import deque
import heapq  # Add this import

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
    return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.
    Your search algorithm needs to return a list of actions that reaches
    the goal. Make sure that you implement the graph search version of DFS,
    which avoids expanding any already visited states. 
    Otherwise your implementation may run infinitely!
    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    """
    Note: Will Utilize Sample Template as a guideline from HW1_Introduction pptx.
    """

    # Initialize closedset
    closedset = []
    # Initialize openset to contain start state and an empty list of actions
    openset = deque([(problem.getStartState(), [])])
    
    # Iterate until openset is empty
    while len(openset) > 0:
        # pop the last state, and actiond from openset
        state, actions = openset.pop()

        # If the state is the goal state, print "Found goal!" and return the actions
        if problem.isGoalState(state):
            print("Found goal!")
            return actions
        
        # If the state is not in the closedset, then append it to the closedset
        if state not in closedset:
            closedset.append(state)

            # For each successor of the state, append the state and the action to the openset
            for (next_state, action, cost) in problem.getSuccessors(state):
                openset.appendleft((next_state, actions + [action]))
    
    # If the openset is empty, return an empty list
    return []
          
          
               


    util.raiseNotDefined()
    

def breadthFirstSearch(problem):
    """
    Note: Will Utilize Sample Template as a guideline from HW1_Introduction pptx.
    """           

    closedset = []
    openset = deque([(problem.getStartState(), [])])

    while len(openset) >  0:
       state, actions = openset.popleft()

       if problem.isGoalState(state):
          print("Found goal!")
          return actions
       
       if state not in closedset:
          closedset.append(state)

          for (next_state, action, cost) in problem.getSuccessors(state):
             openset.append((next_state, actions + [action]))
    
    return []
       



    util.raiseNotDefined()

def uniformCostSearch(problem):
    """
    Note: Will Utilize Sample Template as a guideline from HW1_Introduction pptx.
    """

    closedset = []
    openset = [(0, problem.getStartState(), [])]

    while len(openset) > 0:
       cost, state, actions = heapq.heappop(openset)

       if problem.isGoalState(state):
          print("Found goal!")
          return actions
       
       if state not in closedset:
          closedset.append(state)

          for (next_state, action, next_cost) in problem.getSuccessors(state):
             heapq.heappush(openset, (cost + next_cost, next_state, actions + [action]))
    
    return []
    
    

    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

# TODO:Come back to A* Search and implement it correctly.
def aStarSearch(problem, heuristic=nullHeuristic):
    """
    Note: Will Utilize Sample Template as a guideline from HW1_Introduction pptx.
    """   

    closedset = []
    openset = [(0, problem.getStartState(), [])]

    while len(openset) > 0:
       cost, state, actions = heapq.heappop(openset)

       if problem.isGoalState(state):
          print("Found goal!")
          return actions
       
       if state not in closedset:
          closedset.append(state)
          
          for (next_state, action, next_cost) in problem.getSuccessors(state):
             heapq.heappush(openset, (cost + next_cost + heuristic(next_state, problem), next_state, actions + [action]))

    return []

    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch

def main():
    pass  # This function isn't needed for the Pacman project

if __name__ == "__main__":
   main()
