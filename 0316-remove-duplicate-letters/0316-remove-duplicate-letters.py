from collections import defaultdict

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        d = defaultdict(list)

        for i in range(len(s)):
            d[s[i]].append(i)

        new = []

        for i in range(len(s)):
            x = s[i]
            d[x].pop(0)

            if x in new:
                continue

            while new and new[-1] > x and d[new[-1]] != []:
                new.pop()
            new.append(x)

            
        return ''.join(new)


