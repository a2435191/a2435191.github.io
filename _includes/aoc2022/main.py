import timeit

if __name__ == "__main__":
    from solutions.day16_2 import Solution


    time = timeit.timeit('with open("_includes/aoc2022/inputs/day16_both.txt") as fh: print("RESULT:", Solution.solve([fh.read()]))', globals=globals(), number=1)
    print(time)