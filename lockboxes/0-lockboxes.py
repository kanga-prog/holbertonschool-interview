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
    """
    Determines if all boxes can be opened.

    Args:
        boxes (list of list of int): List of boxes, each containing keys

    Returns:
        bool: True if all boxes can be opened, else False
    """
    if not boxes or type(boxes) is not list:
        return False

    n = len(boxes)
    opened = set([0])      # box 0 is initially opened
    keys = set(boxes[0])   # keys from the first box

    while True:
        opened_before = len(opened)

        for key in list(keys):
            if 0 <= key < n and key not in opened:
                opened.add(key)
                keys.update(boxes[key])

        # Stop if no new boxes were opened
        if len(opened) == opened_before:
            break

    return len(opened) == n
