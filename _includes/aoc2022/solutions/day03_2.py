from BaseSolution import BaseSolution

class Solution(BaseSolution):
    @classmethod
    def solve(cls, inputs: list[str]) -> str:
        input = inputs[0]
        
        total_priority = 0
        lines = input.splitlines()
        for idx in range(0, len(lines), 3):
            elf_group = lines[idx:idx+3]
            elf_group_sets = [set(elf) for elf in elf_group]
            in_common = list(set.intersection(*elf_group_sets))[0]

            priority = ord(in_common)
            if ord('a') <= priority <= ord('z'):
                priority = priority - ord('a') + 1
            elif ord('A') <= priority <= ord('Z'):
                priority = priority - ord('A') + 27

            total_priority += priority
            
        return str(total_priority)