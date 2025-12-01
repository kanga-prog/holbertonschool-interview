#!/usr/bin/python3
"""
0-lockboxes.py

Module that contains a function to determine if all lockboxes can be opened.

Requirements:
- The first box (boxes[0]) is unlocked.
- Each box may contain keys to other boxes.
- A key opens the box with the same number.
"""

def canUnlockAll(boxes):
    if not boxes or type(boxes) != list:
        return False

    n = len(boxes)
    visited = [False] * n  # tracker des boîtes ouvertes

    def dfs(box):
        if visited[box]:
            return
        visited[box] = True
        for key in boxes[box]:
            if 0 <= key < n:
                dfs(key)

    dfs(0)
    return all(visited)
