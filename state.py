import numpy as np


MOVES = {
    "up" : (1, 0),
    "right" : (0, 1),
    "down" : (-1, 0),
    "left" : (0, -1),
}


class State():
    def __init__(self, values : np.array, parent_state) -> None:
        self.values = np.copy(values)
        self._depth = parent_state._depth + 1 if parent_state else 0
        self._path = []
        self._visited = False

    def __eq__(self, other_state) -> bool:
        return np.array_equal(self.values, other_state.values)

    def __hash__(self):
        return hash(self.values.tobytes())

    def display(self) -> None:
        values = self._get_state_tuple()
        string = f"–––––––––––––\n| {values[0]} | {values[1]} | {values[2]} |\n–––––––––––––\n| {values[3]} | {values[4]} | {values[5]} |\n–––––––––––––\n| {values[6]} | {values[7]} | {values[8]} |\n–––––––––––––\n"
        return string

    def get_child_states(self) -> list[tuple]:
        empty_pos = self._get_empty_pos()
        children = []
        for _, (x_shift, y_shift) in MOVES.items():
            new_x = empty_pos[0] + x_shift
            new_y = empty_pos[1] + y_shift
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                new_state = self._swap_positions(empty_pos, (new_x, new_y))
                children.append(new_state)
        return children

    def _swap_positions(self, empty_pos : tuple, swap_pos : tuple):
        new_state = self.copy()
        new_state.values[empty_pos], new_state.values[swap_pos] = new_state.values[swap_pos], new_state.values[empty_pos]
        return new_state

    def copy(self):
        new_state = State(self.values, self)
        new_state._set_path([state for state in self._path] + [self])
        return new_state

    def get_depth(self) -> int:
        return self._depth

    def get_state(self) -> np.array:
        return self.values

    def _get_state_tuple(self) -> tuple:
        return tuple(self.values.flatten())

    def get_path(self) -> list:
        return self._path

    def _set_path(self, parent_states : list) -> None:
        self._path.extend(parent_states)

    def get_visited(self) -> bool:
        return self._visited

    def _get_empty_pos(self) -> tuple:
        return tuple(np.argwhere(self.values == 0)[0])
