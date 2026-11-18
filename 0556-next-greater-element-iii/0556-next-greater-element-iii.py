
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        s = list(str(n))


        pivot = -1
        for i in range(len(s)-2, -1, -1):
            if s[i] < s[i+1]:
                pivot = i
                break

        if pivot == -1:
            return -1


        for i in range(len(s)-1, pivot, -1):
            if s[i] > s[pivot]:
                second = i
                break


        s[pivot], s[second] = s[second], s[pivot]


        s[pivot+1:] = reversed(s[pivot+1:])

        ans = int("".join(s))

        return ans if ans <= 2**31 - 1 else -1
