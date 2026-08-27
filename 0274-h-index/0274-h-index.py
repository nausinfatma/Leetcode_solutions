class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        h = 0

        for i in range(1, n + 1):
            cnt = 0

            for citation in citations:
                if citation >= i:
                    cnt += 1

            if cnt >= i:
                h = i

        return h