
if __name__ == "__main__":
    from solutions.day17_2 import Solution

    with open("_includes/aoc2022/inputs/day17_both.txt") as fh: 
        print("here")
        print("RESULT:", Solution.solve([fh.read()]))


