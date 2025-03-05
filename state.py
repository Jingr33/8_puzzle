""" Script for operation with state class
"""

import numpy as np

# possible shifts
MOVES = {
    "up" : (1, 0),
    "right" : (0, 1),
    "down" : (-1, 0),
    "left" : (0, -1),
}


class State():
    """ Object of one game state. """
    def __init__(self, values : np.array, parent_state : "State") -> None:
        self.values = np.copy(values)
        self._depth = parent_state._depth + 1 if parent_state else 0
        self._path = []
        self._visited = False
        self._heuritstic = None

    def __eq__(self, other_state : "State") -> bool:
        return np.array_equal(self.values, other_state.values)

    def __hash__(self):
        return hash(self.values.tobytes())

    def get_child_states(self) -> list["State"]:
        """ Find all child (next possible) states of current state.
        
        Return:
            list[State]: list of child states 
        """
        empty_pos = self._get_empty_pos()
        children = []
        for _, (x_shift, y_shift) in MOVES.items():
            new_x = empty_pos[0] + x_shift
            new_y = empty_pos[1] + y_shift
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                new_state = self._swap_positions(empty_pos, (new_x, new_y))
                children.append(new_state)
        return children

    def _swap_positions(self, empty_pos : tuple, swap_pos : tuple) -> "State":
        """ Create copy of current state and swap one value with empty position.
        
        Args:
            empty_pos : tuple
                index of empty position in state matrix
            swap_pos : tuple
                index of neighbor swap position

        Return:
            State: new child state
        """
        new_state = self.copy()
        new_state.values[empty_pos], new_state.values[swap_pos] = new_state.values[swap_pos], new_state.values[empty_pos]
        return new_state

    def copy(self) -> "State":
        """ Create copy of current state, add current state to new state path
        
        Return:
            State: a new copied state
        """
        new_state = State(self.values, self)
        new_state._set_path(self._path + [self])
        return new_state

    def set_heuristic_cost(self, goal : "State") -> None:
        """ Count Manhattan heuristic cost of path from this state to goal state.
        
        Args:
            goal : State
                a goal state object
        """
        cost = 0
        for number in range(1, 9):
            real_idx = np.where(self.values == number)
            goal_idx = np.where(goal.values == number)
            cost += np.abs(real_idx[0] - goal_idx[0]) + np.abs(real_idx[1] - goal_idx[1])
        self._heuritstic = cost

    def get_depth(self) -> int:
        """Get depth."""
        return self._depth

    def get_state(self) -> np.array:
        """Get state"""
        return self.values

    def _get_state_tuple(self) -> tuple:
        return tuple(self.values.flatten())

    def get_path(self) -> list:
        """Get path"""
        return self._path

    def _set_path(self, parent_states : list) -> None:
        self._path.extend(parent_states)

    def get_visited(self) -> bool:
        """Get visited"""
        return self._visited

    def _get_empty_pos(self) -> tuple:
        return tuple(np.argwhere(self.values == 0)[0])

    def get_heuristic(self) -> int:
        """ Get hueristic. """
        return self._heuritstic