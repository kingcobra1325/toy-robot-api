MAX_TABLE_X = 10
MAX_TABLE_Y = 10

def move_north(toy: dict):
    if toy["y"] < MAX_TABLE_Y:
        toy["y"] += 1

def move_south(toy: dict):
    if toy["y"] > 0:
        toy["y"] -= 1

def move_west(toy: dict):
    if toy["x"] > 0:
        toy["x"] -= 1

def move_east(toy: dict):
    if toy["x"] < MAX_TABLE_X:
        toy["x"] += 1

MOVEMENT_MAP = {
    "north": move_north,
    "south": move_south,
    "west": move_west,
    "east": move_east,
}

def turn_from_north(toy: dict, direction: str):
    if direction == "left":
        toy["face"] = "west"
    else:
        toy["face"] = "east"

def turn_from_south(toy: dict, direction: str):
    if direction == "left":
        toy["face"] = "east"
    else:
        toy["face"] = "west"

def turn_from_west(toy: dict, direction: str):
    if direction == "left":
        toy["face"] = "south"
    else:
        toy["face"] = "north"

def turn_from_east(toy: dict, direction: str):
    if direction == "left":
        toy["face"] = "north"
    else:
        toy["face"] = "south"

TURNING_MAP = {
    "north": turn_from_north,
    "south": turn_from_south,
    "west": turn_from_west,
    "east": turn_from_east,
}

def move_toy(toy: dict):
    func = MOVEMENT_MAP[toy["face"]]
    func(toy) # type: ignore

def turn_toy(toy: dict, direction: str):
    func = TURNING_MAP[toy["face"]]
    func(toy, direction) # type: ignore