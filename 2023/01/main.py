def Calibration(calibration_list: list[str]) -> int:
    total: int = 0
    for string in calibration_list:
        num_only: list[str] = []
        for char in string:
            if char.isdigit():
                num_only.append(char)
        left: str = num_only[0]
        right: str = num_only[-1]
        actual: str = left + right
        final = int(actual)
        total = total + final
    return total


def main():
    with open("input.txt", "r") as f:
        calibration_list = [line.strip() for line in f]
    print(Calibration(calibration_list))


if __name__ == "__main__":
    main()
