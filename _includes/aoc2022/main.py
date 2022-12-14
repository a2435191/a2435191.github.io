if __name__ == "__main__":
    from solutions.day14_1 import Solution

    with open("_includes/aoc2022/inputs/day14_both.txt") as fh:
        print(Solution.solve([fh.read()]))