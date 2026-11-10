class Solution:
    def findLongestWord(self, s: str, dictionary: list[str]) -> str:
        
        ans = ''
        

        for x in dictionary:
            flag = True
            temp = list(s)
            idx = -1
            for y in x:
                
                if y in temp[idx+1:]:
                    idx = temp.index(y, idx+1)
                    
                else:
                    flag = False
                    break

            if flag == True:
                if len(x) > len(ans):
                    ans = x

                elif len(x) == len(ans):
                    ans = min(x, ans)


        return ans

