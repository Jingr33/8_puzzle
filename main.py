"""Sliding number puzzle."""

import numpy as np
from icecream import ic

from state import State
from tree import Tree


INITIAL_STATE = State(np.array([[2, 8, 3],
                                [0, 1, 4],
                                [7, 6, 5]]), None)

GOAL_STATE = State(np.array([[1, 2, 3],
                             [8, 0, 4],
                             [7, 6, 5]]), None)

MAX_DEPTH = 5

def depth_first_search(state : State, tree : Tree, visited : set):
    if state in visited:
        return None
    
    visited.add(state)
    state.add_state_to_path(state)
    tree.add_to_tree(state)

    # check goal state
    if state == GOAL_STATE:
        ic("GOAL")
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
tree.display_tree()