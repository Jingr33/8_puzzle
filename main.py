"""Sliding number puzzle."""

import numpy as np
from typing import Optional

from state import State
from tree import Tree


INITIAL_STATE = State(np.array([[2, 8, 3],
                                [0, 1, 4],
                                [7, 6, 5]]), None)

GOAL_STATE = State(np.array([[1, 2, 3],
                             [8, 0, 4],
                             [7, 6, 5]]), None)

MAX_DEPTH = 10

def depth_first_search(state : State, tree : Tree, visited : set) -> Optional[State]:
    """ Recursive function finds solution to 8 puzzles using depth first search algorithm.

    Args:
        state : State
            the currently browsed state
        tree : Tree
            object storing the history of browsing through the algorithm
        visited : set
            set of all visited states

    Return:
        Optional[State]: return final state if goal is found, otherwise None 
    """
    if state in visited:
        return None
    
    visited.add(state)
    tree.add_to_tree(state)

    # check goal state
    if state == GOAL_STATE:
        print("Target successfully found!")
        return state
    
    # max depth
    if state.get_depth() >= MAX_DEPTH:
        return None

    # new iter
    for child_state in state.get_child_states():
        if not child_state.get_visited():
            result = depth_first_search(child_state, tree, visited)
            if result:
                return result
    
    return None

visited = set()
tree = Tree()
reuslt = depth_first_search(INITIAL_STATE, tree, visited)
tree.draw_tree(6, reuslt)
