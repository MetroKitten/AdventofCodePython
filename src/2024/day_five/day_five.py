iterations: int = 0


def check_meets_rules(pages: list[int], rules: list[tuple[int, int]]) -> bool:
    for high, low in rules:
        if high in pages and low in pages:
            high_index = pages.index(high)
            low_index = pages.index(low)
            if high_index >= low_index:
                return False
    return True


def fix_failing_pages(pages: list[int], rules: list[tuple[int, int]]):
    global iterations
    iterations = iterations + 1
    failed_page = pages.copy()
    if check_meets_rules(failed_page, rules):
        return failed_page

    for high, low in rules:
        if high in failed_page and low in failed_page:
            high_index = failed_page.index(high)
            low_index = failed_page.index(low)
            if high_index >= low_index:
                failed_page[high_index], failed_page[low_index] = (
                    failed_page[low_index],
                    failed_page[high_index],
                )
                result = fix_failing_pages(failed_page, rules)
                if result:
                    return result
    return False


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
        fixed_pages_total: int = 0
        failed_pages: list[list[int]] = []
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
            else:
                failed_pages.append(page)

        for page in failed_pages:
            corrected_page: list[int] = fix_failing_pages(page, rules)
            fixed_pages_total += calc_middle_totals(corrected_page)

        print(f"Correct Page Total: {correct_pages_total}")
        print(f"Fixed Page Total: {fixed_pages_total}")
        print(f"Recursive Iterations: {iterations}")


if __name__ == "__main__":
    main()
