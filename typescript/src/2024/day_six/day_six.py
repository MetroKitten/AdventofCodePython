from enum import Enum


class Directions(Enum):
    LEFT = (0, -1)
    RIGHT = (1, 0)
    UP = (-1, 0)
    DOWN = (1, 0)


class Obstacle(Enum):
    OBSTACLE1 = "#"


class Guard(Enum):
    GUARD1 = "^"


def get_grid_bounds(grid: list[list[str]]) -> tuple[int, int]:
    rows = len(grid)
    cols = len(grid[0])
    return rows, cols


def get_guard_position(grid: list[list[str]], guard: Guard) -> tuple[int, int]:
    return guard_position


def navigate_route(grid, gridbounds, guard_position) -> int:
    steps = 0
    direction = Directions.UP
    """
        Check moving direction
        If direction is an obstacle turn and check, if clear move, steps ++
        If direction is OoBs return steps
    """

    return steps


def main():
    with open("./input.txt", "r") as f:
        file = f.read()
        matrix = [list(line) for line in file.split("\n") if line.strip()]


if __name__ == "__main__":
    main()
