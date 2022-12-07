if __name__ == "__main__":
    from solutions.day07_2 import Solution

    with open("_includes/aoc2022/inputs/day07_both.txt") as fh:
        print(Solution.solve([fh.read()]))