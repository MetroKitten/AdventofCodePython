def total_distance(left_list: list[int], right_list: list[int]) -> int:
    left_sorted = sorted(left_list)
    right_sorted = sorted(right_list)
    total_distance: int = 0
    for left_item, right_item in zip(left_sorted, right_sorted):
        difference: int = max(left_item, right_item) - min(left_item, right_item)
        total_distance += difference
    return total_distance


def similarity_score(left_list: list[int], right_list: list[int]) -> int:
    total: int = 0
    for left_item in left_list:
        occurances = right_list.count(left_item)
        total += left_item * occurances
    return total


def main():
    with open("./input.txt", "r") as f:
        left_list: list[int] = []
        right_list: list[int] = []
        for line in f:
            parts = line.split(None, 1)
            left_num = int(parts[0])
            right_num = int(parts[1])
            left_list.append(left_num)
            right_list.append(right_num)

    total = total_distance(left_list, right_list)
    similarity = similarity_score(left_list, right_list)
    print(f"Total Distance is: {total}")
    print(f"Similarity Score is: {similarity}")


if __name__ == "__main__":
    main()
