import numpy as np
import tkinter as tk
from icecream import ic

from state import State


class Tree():
    def __init__(self)-> None:
        self._root = tk.Tk()
        self._canvas = tk.Canvas(self._root, width=1250, height=750, bg="white")
        self._canvas.pack()
        self._tree = {}

    def add_to_tree(self, state : State) -> None:
        depth = state.get_depth()
        if not depth in self._tree:
            self._tree[depth] = []
        self._tree[depth].append(state)

    def display_tree(self, max_depth : int) -> None:
        depths = [i for i in range(max_depth + 1)]
        for depth in depths:
            print(f"Depth {depth}:")
            print(len(self._tree[depth]))
            # for state in self._tree[depth]:
                # print(state.display())

    def draw_tree(self, max_depth : int) -> None:
        self.draw_state(self._canvas, self._tree[0][0])

        self._root.mainloop()

    def draw_state(self, canvas, state : State) -> None:
        """Nakreslí jeden stav v gridu na zadané souřadnice."""
        values = state.values
        x, y = 20, 20
        site = 25
        for i in range(3):
            for j in range(3):
                text = "" if values[i, j] == 0 else str(values[i, j])
                canvas.create_rectangle(x + j * site, y + i * site, x + (j + 1) * site, y + (i + 1) * site, fill="white", outline="black")
                canvas.create_text(x + j * site + 13, y + i * site + 13, text=text, font=("Arial", 14))