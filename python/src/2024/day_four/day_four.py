def get_grid_bounds(grid: list[list[str]]) -> tuple[int, int]:
    rows = len(grid)
    cols = len(grid[0])
    return rows, cols


def search_grid(grid: list[list[str]]) -> int:
    """Iterate through the items in the grid"""
    count = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            count += navigate_grid(grid, row, col)
    return count


def navigate_grid(
    grid: list[list[str]], starting_row: int, starting_column: int
) -> int:
    """Move in different directions"""
    word = "MAS"
    count = 0
    directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    for row_move, column_move in directions:
        if check_mas(grid, starting_row, starting_column, word, row_move, column_move):
            count += 1

    return count


def check_xmas(
    grid: list[list[str]],
    starting_row: int,
    starting_column: int,
    word: str,
    row_move: int,
    column_move: int,
) -> bool:
    """Find XMAS within grid"""
    word_length = len(word)
    rows, cols = get_grid_bounds(grid)
    for i in range(word_length):
        new_row = starting_row + i * row_move
        new_col = starting_column + i * column_move
        if new_row < 0 or new_row >= rows or new_col < 0 or new_col >= cols:
            return False

    for i in range(word_length):
        new_row = starting_row + i * row_move
        new_col = starting_column + i * column_move
        if grid[new_row][new_col] != word[i]:
            return False

    return True


def check_mas(
    grid: list[list[str]],
    starting_row: int,
    starting_column: int,
    word: str,
    row_move: int,
    column_move: int,
) -> bool:
    """Find MAS in an X Shape"""
    rows, cols = get_grid_bounds(grid)
    positions = [
        (starting_row, starting_column),
        (starting_row + row_move, starting_column + column_move),
        (starting_row - row_move, starting_column - column_move),
    ]

    for new_row, new_col in positions:
        if new_row < 0 or new_row >= rows or new_col < 0 or new_col >= cols:
            return False

    if grid[starting_row][starting_column] != word[1]:
        return False
    if grid[starting_row + row_move][starting_column + column_move] != word[0]:
        return False
    if grid[starting_row - row_move][starting_column - column_move] != word[2]:
        return False

    return True


def main():
    with open("./input.txt", "r") as f:
        file = f.read()
        xmas_matrix = [list(line) for line in file.split("\n") if line.strip()]
        count = search_grid(xmas_matrix)
        print(f"Total XMAS Found: {count}")


if __name__ == "__main__":
    main()
