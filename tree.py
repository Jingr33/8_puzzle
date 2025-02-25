import numpy as np
from icecream import ic

from state import State


class Tree():
    def __init__(self)-> None:
        self._tree = {}

    def add_to_tree(self, state : State) -> None:
        depth = state.get_depth()
        if not depth in self._tree:
            self._tree[depth] = []
        self._tree[depth].append(state)

    def display_tree(self) -> None:
        for depth in self._tree.keys():
            print(f"Depth {depth}:")
            print(len(self._tree[depth]))
            # for state in self._tree[depth]:
                # print(state.display())
