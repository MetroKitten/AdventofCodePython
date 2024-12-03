import regex


def find_muls(text: str) -> int:
    uncorrupted = 0
    matches: list[tuple[str, str]] = regex.findall(r"mul\((\d+),(\d+)\)", text)
    for match in matches:
        left, right = map(int, match)
        uncorrupted += left * right
    return uncorrupted


def find_muls_v2(text: str) -> int:
    matches: list[str] = regex.split(r"(?<=mul\(\d+,\d+\))", text)
    disabled_strings: list[str] = []
    enabled_strings: list[str] = []
    enabled: bool = True
    uncorrupted = 0
    for line in matches:
        if "don't()" in line:
            enabled = False
        elif "do()" in line:
            enabled = True
        if enabled:
            enabled_strings.append(line)
        else:
            disabled_strings.append(line)
    for string in enabled_strings:
        uncorrupted += find_muls(string)
    return uncorrupted


def main():
    with open("./input.txt", "r") as f:
        file = f.read()
    print(f"Uncorrupted Total: {find_muls_v2(file)}")


if __name__ == "__main__":
    main()
