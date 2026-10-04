from collections import deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:
        if startGene == endGene:
            return 0

        bank = set(bank)

        if endGene not in bank:
            return -1

        q = deque([(startGene, 0)])
        visited = {startGene}

        while q:
            gene, steps = q.popleft()

            if gene == endGene:
                return steps

            for next_gene in bank:
                if next_gene not in visited:
                    diff = sum(a != b for a, b in zip(gene, next_gene))

                    if diff == 1:
                        visited.add(next_gene)
                        q.append((next_gene, steps + 1))

        return -1
