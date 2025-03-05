""" State object test script
"""

import numpy as np

from state import State


def test_state_initialization():
    """ INItialization testing"""
    values = np.array([[1, 2, 3], [4, 0, 5], [6, 7, 8]])
    state1 = State(values, None)
    state2 = State(values, state1)

    assert np.array_equal(state1.values, values)
    assert  state1.get_depth() == 0
    assert state2.get_depth() == 1

def test_state___eq__():
    """ State equation test """
    values1 = np.array([[1, 2, 3], [4, 0, 5], [6, 7, 8]])
    values2 = np.array([[1, 2, 3], [4, 0, 5], [6, 7, 8]])
    values3 = np.array([[3, 1, 2], [4, 0, 5], [6, 7, 8]])

    state1 = State(values1, None)
    state2 = State(values2, None)
    state3 = State(values3, None)

    assert state1 == state2
    assert state1 != state3 

def test_state_copy():
    """ State.copy() instance test """
    values = np.array([[1, 2, 3], [4, 0, 5], [6, 7, 8]])
    state = State(values, None)
    new_state = state.copy()

    assert state == new_state
    assert state.get_path() != new_state.get_path()

def test_state_get_child_state():
    """ State.get_child_state test """
    values = np.array([[1, 2, 3], [4, 0, 5], [6, 7, 8]])
    state = State(values, None)
    child_states = [State(np.array([[1, 2, 3], [4, 5, 0], [6, 7, 8]]), state), 
                    State(np.array([[1, 2, 3], [0, 4, 5], [6, 7, 8]]), state), 
                    State(np.array([[1, 2, 3], [4, 7, 5], [6, 0, 8]]), state), 
                    State(np.array([[1, 0, 3], [4, 2, 5], [6, 7, 8]]), state)]
    
    children = state.get_child_states()

    assert len(children) == 4
    for child in children:
        assert child in child_states

def test_set_heuristic_cost():
    """ State.set_heuristic_cost test """
    state = State(np.array([[1, 2, 3], [4, 5, 0], [6, 7, 8]]), None)
    goal = State(np.array([[1, 2, 3], [8, 0, 4], [7, 6, 5]]), None)

    state.set_heuristic_cost(goal)
    
    assert state.get_heuristic() == 9