class Solution:
    def maxProduct(self, words: List[str]) -> int:

        maxm = 0
        
        for i in range(len(words)-1):
            for j in range(i+1, len(words)):
                if not set(words[i]) & set(words[j]):
                    maxm = max(maxm, len(words[i])*len(words[j])) 

        return maxm