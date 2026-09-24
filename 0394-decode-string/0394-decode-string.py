class Solution:
    def decodeString(self, s: str) -> str:
        
        i = 0

        def decode():
            nonlocal i

            result = ""

            while i < len(s) and s[i] != ']':
                if s[i].isalpha():
                    result += s[i] 
                    i += 1

                else:

                    k = 0
                    while i < len(s) and s[i].isdigit():
                        k = k * 10 + int(s[i])
                        i += 1

                    i += 1

                    decoded = decode()

                    i += 1

                    result += decoded * k

            return result

        return decode()