class Solution:
    def lexicalOrder(self, n: int) -> list[int]:
        
        arr = []
        for i in range(1, n+1):
            arr.append(str(i))

        arr.sort()
        arr = list(map(int, arr))
        return arr
        
