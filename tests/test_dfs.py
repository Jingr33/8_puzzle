""" DFS testing script
"""

from main import INITIAL_STATE, GOAL_STATE, depth_first_search
from tree import Tree

def test_depth_first_search():
    """ DFS test """
    visited = set()
    tree = Tree()
    result = depth_first_search(INITIAL_STATE, tree, visited)

    assert result == GOAL_STATE
