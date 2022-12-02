from abc import ABC, abstractmethod

class BaseSolution(ABC):
    """
    Base class representing an Advent of Code solution.
    """

    @classmethod
    @abstractmethod
    def solve(cls, inputs: list[str]) -> str:
        """Solve an AOC problem.

        Args:
            inputs (list[str]): 
            Problem input, represented as a list of strings. Usually length one.

        Returns:
            str: String representation of the answer.
        """
        pass