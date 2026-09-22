class Solution:
    def lengthLongestPath(self, input: str) -> int:
        path = input.split('\n')
        stack = []
        n = 0

        for x in path:
            cnt = x.count('\t')
            stack = stack[:cnt]
            name = x.strip('\t')
            stack.append(name)

            if '.' in  name:
                new = '/'.join(stack)
                n = max(n, len(new))

        return n