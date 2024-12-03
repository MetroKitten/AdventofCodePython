import re


def find_muls(text: str):
    uncorrupted = 0
    matches: list[tuple[str, str]] = re.findall(r"mul\((\d+),(\d+)\)", text)
    for match in matches:
        left, right = map(int, match)
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
