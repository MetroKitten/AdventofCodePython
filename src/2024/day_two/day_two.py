def is_safe_report(report_line: list[int]) -> bool:
    is_ascending = all(a < b for a, b in zip(report_line, report_line[1:]))
    is_descending = all(a > b for a, b in zip(report_line, report_line[1:]))
    right_diff = all(abs(a - b) <= 3 for a, b in zip(report_line, report_line[1:]))
    return (is_ascending or is_descending) and right_diff


def main():
    with open("./input.txt", "r") as f:
        safe_reports: int = 0
        for line in f:
            part = [int(x) for x in line.split()]
            if is_safe_report(part):
                safe_reports += 1
            else:
                for i in range(len(part)):
                    chopped_list = part[:i] + part[i + 1 :]
                    if is_safe_report(chopped_list):
                        safe_reports += 1
                        break
        print(f"Total Safe Reports {safe_reports}")


if __name__ == "__main__":
    main()
