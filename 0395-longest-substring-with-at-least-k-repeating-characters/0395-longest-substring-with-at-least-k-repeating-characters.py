class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        
        cnt = 0
        s1 = ''

        for i in range(len(s)):
            s1 = ''
            freq = {}

            for j in range(i, len(s)):
                s1 += s[j]

                if s[j] in freq:
                    freq[s[j]] += 1
                else:
                    freq[s[j]] = 1

                valid = True

                for ch in freq:
                    if freq[ch] < k:
                        valid = False
                        break

                if valid:
                    if len(s1) > cnt:
                        cnt = len(s1)

        return cnt

