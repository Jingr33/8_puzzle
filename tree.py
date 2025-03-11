""" Script for operation with Tree class
"""

import tkinter as tk
from icecream import ic

from state import State

WIN_WIDTH, WIN_HEIGHT = 1250, 750


class Tree():
    """ Class for storage and display whole path of algorithm through visited states """
    def __init__(self)-> None:
        self._root = tk.Tk()
        self._root.title("Tree structure of depth first search")
        self._canvas = tk.Canvas(self._root, width=WIN_WIDTH, height=WIN_HEIGHT, bg="white")
        self._canvas.pack()
        self._tree = {}

    def add_to_tree(self, state : State) -> None:
        """ Add state into tree structure. 
        
        Args:
            state : State
                state object
        """
        depth = state.get_depth()
        if not depth in self._tree:
            self._tree[depth] = []
        self._tree[depth].append(state)

    def draw_tree(self, max_depth : int, goal : State) -> None:
        """ Draw and display whole algorithm tree path. 
        
        Args:
            max_depth : int
                number of displayed depth layers
            goal : State
                goal state object
        """
        max_depth = min(max_depth, max(self._tree.keys()) + 1)
        depths = list(range(max_depth))
        for depth in depths:
            states_count = len(self._tree[depth])
            (x_pos_list, y_pos) = self._get_state_pos(max_depth, depth, states_count)

            for j in range(len(self._tree[depth])):
                self._draw_state(self._canvas, self._tree[depth][j], x_pos_list[j], y_pos, goal)
                self._draw_connection(self._tree[depth][j], (x_pos_list[j], y_pos), max_depth)
                self._draw_heuristic(self._tree[depth][j], (x_pos_list[j], y_pos))

        self._root.mainloop()

    def _draw_state(self, canvas : tk.Canvas, state : State, x : int, y : int, goal : State) -> None:
        """ Draw a matrix of an entered state into the tree.
        
        Args:
            canvas : tk.Canvas
                tkinter canvas
            state : State
                a state to draw
            x : int
                horizontal position of the state in the canvas
            y : int
                vertical position of the state in the canvas
            goal : State
                goal state object
        """
        values = state.values
        site = 25
        for i in range(3):
            for j in range(3):
                text = "" if values[i, j] == 0 else str(values[i, j])
                canvas.create_rectangle(x + j * site, y + i * site, x + (j + 1) * site, y + (i + 1) * site, fill="white", outline="black")
                canvas.create_text(x + j * site + 13, y + i * site + 13, text=text, font=("Arial", 14))

                self._check_and_draw_goal(state, x, y, goal)

    def _draw_connection(self, state : State, p1 : tuple[int], max_depth : int) -> None:
        """ Draw connection line between child and parent state.

        Args:
            state : State
                end state of the connection (child)
            p1 : tuple[int]
                positon of the child state
            max_depth : int
                nuber of displayed depth layers 
         """
        if not state.get_path():
            return

        parent_state = state.get_path()[-1]
        parent_depth = parent_state.get_depth()

        pos = None
        states_depth_count = len(self._tree[parent_depth])
        for i in range(states_depth_count):
            if parent_state == self._tree[parent_depth][i]:
                pos = i

        if pos is not None:
            (x_poses, y_pos) = self._get_state_pos(max_depth, parent_depth, states_depth_count)
            p2 = (x_poses[pos], y_pos)
            self._canvas.create_line(p1[0] + 38, p1[1], p2[0] + 38 , p2[1] + 75)

    def _get_state_pos(self, max_depth : int, depth : int, state_cnt : int) -> tuple[int]:
        """ Return top left positons of states of specific depth.
        
        Args:
            max_depth : int
                nuber of displayed depth layers 
            depth : int
                depth attributte of the state
            state_cnt : int
                number of states in entered depth

        Return:
            tuple[int]: (x_positions - all postions in row, y_positon)
        """
        x_positions = [WIN_WIDTH/state_cnt * pos + WIN_WIDTH/state_cnt/2 - 35 for pos in range(state_cnt)]
        y_position = WIN_HEIGHT / max_depth * depth + 10
        return (x_positions, y_position)

    def _check_and_draw_goal (self, state : State, x : int, y : int, goal : State) -> None:
        """ Check if this state is a goal state, if yes, marks it with a yellow square.
        
        Args:
            state : State
                current state
            x : int
                horizontal position of the state
            y : int
                vertical position of the state
            goal : State
                goal state
            """
        if state == goal:
            self._canvas.create_rectangle(x - 5, y - 5, x + 82, y + 82, outline="gold", width = 4)

    def _draw_heuristic(self, state : State, position : tuple[int]) -> None:
        """ Write heuristic values of the state.
        
        Args:
            state : State
                the state of interest
            position : tuple[int]
                (x, y) position of the top left corner of the state
        """
        if state.get_heuristic() is None:
            return
        
        x, y = position[0] - 28, position[1] + 40
        heuristic_str = f"{state.get_depth()} + {state.get_heuristic()[0]}"
        self._canvas.create_text(x, y, text = heuristic_str, font = "Times 12")