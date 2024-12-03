import re


def find_muls(text: str):
    list_of_muls: list[tuple[str, str]] = []
    uncorrupted = 0
    matches: list[tuple[str, str]] = re.findall(r"mul\((\d+),(\d+)\)", text)
    for match in matches:
        list_of_muls.append(match)
    for pair in list_of_muls:
        left = int(pair[0])
        right = int(pair[1])
        uncorrupted += left * right
    return uncorrupted


def main():
    with open("./input.txt", "r") as f:
        total = 0
        for line in f:
            matches = find_muls(line)
            total += matches

    print(f"Uncorrupted Total: {total}")


if __name__ == "__main__":
    main()
