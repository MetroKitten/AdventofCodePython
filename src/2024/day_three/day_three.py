import re


def main():
    with open("./input.txt", "r") as f:
        list_of_muls = []
        uncorrupted = 0
        for line in f:
            matches = re.findall(r"mul\((\d+),(\d+)\)", line)
            for match in matches:
                list_of_muls.append(match)
        for pair in list_of_muls:
            left = int(pair[0])
            right = int(pair[1])
            uncorrupted += left * right
    print(f"Uncorrupted Total: {uncorrupted}")


if __name__ == "__main__":
    main()
