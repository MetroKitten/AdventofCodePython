def check_meets_rules(pages: list[int], rules: list[tuple[int, int]]) -> bool:
    for high, low in rules:
        if high in pages and low in pages:
            high_index = pages.index(high)
            low_index = pages.index(low)
            if high_index >= low_index:
                return False
    return True


def calc_middle_totals(correct_pages: list[int]) -> int:
    middle_total = 0
    if len(correct_pages) % 2 == 0:
        print("Even")
    else:
        middle_index = len(correct_pages) // 2
        middle_total += correct_pages[middle_index]
    return middle_total


def main() -> None:
    with open("./input.txt", "r") as f:
        correct_pages_total: int = 0
        rules: list[tuple[int, int]] = []
        pages: list[list[int]] = []
        file = f.read()
        raw_rules, raw_pages = file.split("\n\n")

        for rule in raw_rules.splitlines():
            rule_parts: list[str] = rule.strip().split("|")
            rules.append(tuple(map(int, rule_parts)))

        for page in raw_pages.splitlines():
            parts: list[str] = page.strip().split(",")
            pages.append(list(map(int, parts)))

        for page in pages:
            if check_meets_rules(page, rules):
                correct_pages_total += calc_middle_totals(page)

        print(f"Correct Page Total: {correct_pages_total}")


if __name__ == "__main__":
    main()
