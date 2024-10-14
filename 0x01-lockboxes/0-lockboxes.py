#!/usr/bin/python3
"""
0. Lockboxes . determine if all boxes can be opened
"""


def canUnlockAll(boxes):
    """
    Write a method that determines if all the `boxes` can be opened.
    """
    keys = [0]  # a set that contains the keys found
    keys.extend(boxes[0])
    can_open = []
    unopened = []
    for key, box in enumerate(boxes):
        if key in keys:
            keys.extend(box)
            can_open.append(True)
        else:
            unopened.append({key: box})
            can_open.append(False)
    # try to open boxes with remaining keys
    for d in unopened:
        for key in d:
            if key in keys:
                can_open.pop(key)
                keys.extend(d[key])
                can_open.insert(key, True)

    return False if False in can_open else True
