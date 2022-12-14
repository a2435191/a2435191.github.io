# day13_common.py

from BaseSolution import BaseSolution


def packets_in_order(left: list[list | int], right: list[list | int]) -> bool | None:
    # If both values are lists, compare element-wise
    for x, y in zip(left, right):
        if isinstance(x, int) and isinstance(y, int):
            if x > y:
                # if both values are integers and the left is bigger than the right,
                # they're out of order, so abort immediately
                return False
            # otherwise if left < right, comparison is good.
            elif x < y:
                return True
            # if left == right, it is undetermined, so we keep checking input
        else:
            # if exactly one is a list and the other is an int, put the int in a list
            if isinstance(x, int):
                x = [x]
            if isinstance(y, int):
                y = [y]

            # then compare their results
            in_order = packets_in_order(x, y)
            if in_order is not None:
                return in_order

    # we have reached no comparisons that yield True or False, so now we must compare length
    if len(left) < len(right):
        return True
    if len(left) > len(right):
        return False
    return None  # still undetermined
