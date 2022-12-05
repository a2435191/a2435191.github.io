if __name__ == "__main__":
    from solutions.day05_2 import Solution

    with open("_includes/aoc2022/inputs/day05_both.txt") as fh:
        print(Solution.solve([fh.read()]))