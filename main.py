"""Sliding number puzzle."""

from typing import Optional
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

MAX_DEPTH = 10

def a_star_search(state : State, tree : Tree) -> Optional[State]:
    """ Recursive funciton finds solution to 8 puzzle using A* search algorithm with Manhattan heuristic.
    
    Args:
        state : State
            the currently browsed state
        tree : Tree
            object storing the history of browsing through the algorithm

    Return:
        Optional[State]: return final state if goal is found, otherwise None
    """
    if state.get_depth() == 0:
        state.set_heuristic_cost(GOAL_STATE)
        tree.add_to_tree(state)

    # check goal state
    if state.get_heuristic() == 0:
        print("Target was successfully found with A*!")
        return state
    
    # max depth check
    if state.get_depth() >= MAX_DEPTH:
        return None
    
    children = []
    for child in state.get_child_states():
        child.set_heuristic_cost(GOAL_STATE)
        children.append(child)
        tree.add_to_tree(child)
    cheapest = min(children, key = lambda one_state: one_state.get_heuristic())
    result = a_star_search(cheapest, tree)
    if result:
        return result

    return None


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
        print("Target successfully found with DFS!")
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

visited_empty = set()
tree_empty = Tree()
result = a_star_search(INITIAL_STATE, tree_empty)
tree_empty.draw_tree(6, result)
