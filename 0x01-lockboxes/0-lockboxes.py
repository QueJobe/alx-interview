#!/usr/bin/python3
"""
Determine if all boxes can be unlocked
"""


def canUnlockAll(boxes):
    """
    function to check if boxes can be unlocked
    """
    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True
    keys = [0]

    while keys:
        current_box = keys.pop(0)
        
        for key in boxes[current_box]:
            if key < n and not unlocked[key]:
                unlocked[key] = True
                keys.append(key)

    return (all(unlocked))
