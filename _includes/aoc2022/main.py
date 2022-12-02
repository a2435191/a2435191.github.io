if __name__ == "__main__":
    from solutions.day02_2 import Solution

    with open("_includes/aoc2022/inputs/day02_both.txt") as fh:
        print(Solution.solve([fh.read()]))