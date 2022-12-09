from BaseSolution import BaseSolution

class Solution(BaseSolution):
    @staticmethod
    def _parse_input(lines: list[str]) -> list[list[int]]:
        return [[int(n) for n in line] for line in lines]

    @classmethod
    def solve(cls, inputs: list[str]) -> str:
        heights = Solution._parse_input(inputs[0].splitlines())

        array_width = len(heights[0])
        array_height = len(heights)

        view_scores: dict[tuple[int, int], int] = {}

        for i, row in enumerate(heights):
            for j, height in enumerate(row):
                view_score = 1
                view_scores_lst = []

                # max views to the right
                max_viewing_distance = 0
                for neighbor_height in row[j+1:]:
                    max_viewing_distance += 1
                    if neighbor_height >= height:
                        break
                view_score *= max_viewing_distance
                view_scores_lst.append(max_viewing_distance)

                # to the left
                max_viewing_distance = 0
                for neighbor_height in reversed(row[:j]):
                    max_viewing_distance += 1
                    if neighbor_height >= height:
                        break
                view_score *= max_viewing_distance
                view_scores_lst.append(max_viewing_distance)

                # to the top
                max_viewing_distance = 0
                for neighbor_i in reversed(range(i)):
                    max_viewing_distance += 1

                    neighbor_height = heights[neighbor_i][j]
                    if neighbor_height >= height:
                        break
                view_score *= max_viewing_distance
                view_scores_lst.append(max_viewing_distance)

                # to the bottom
                max_viewing_distance = 0
                for neighbor_i in range(i + 1, array_height):
                    max_viewing_distance += 1

                    neighbor_height = heights[neighbor_i][j]
                    if neighbor_height >= height:
                        break
                view_score *= max_viewing_distance
                view_scores_lst.append(max_viewing_distance)

                view_scores[(i, j)] = view_score

        return max(view_scores.values())
