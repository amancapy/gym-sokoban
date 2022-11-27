import random
import numpy as np
import marshal
import os


def inter(arr):
    arr = [list(row) for row in arr]
    arr = [[int(char
                .replace(" ", "0")
                .replace("@", "1")
                .replace("+", "2")
                .replace("#", "3")
                .replace("$", "4")
                .replace(".", "5")
                .replace("*", "6"))
            for char in row] for row in arr]
    return np.array(arr, dtype=np.uint8)

def generate_room(dim=(26, 26), p_change_directions=0.35, num_steps=25, num_boxes=3, tries=4, second_player=False):
    pick = f"xsbs/{random.randint(1, 15)}/{random.randint(1, 100)}.xsb"
    while not os.path.exists(pick):
        pick = f"xsbs/{random.randint(1, 15)}/{random.randint(1, 100)}.xsb"
    room_state = open(pick).read().split("\n\n")
    lname = pick.split("/")[0] + "/" + room_state[0].split("; ")[1]
    room_state = room_state[1].split("\n")
    room_state = [list(row + " " * (26 - len(row))) for row in room_state if row]
    room_state += [" " * 26] * (26 - len(room_state))
    for _ in range(random.choice([0, 1, 2, 3])):
        room_state = list(zip(*room_state[::-1]))
    room_state = inter(room_state)

    room_structure = np.array(room_state)
    room_structure[(room_structure == 1) | (room_structure == 2) | (room_structure == 4)] = 0
    room_structure[(room_structure == 6)] = 5
    room_state[(room_state == 2)] = 1
    return room_structure, room_state

