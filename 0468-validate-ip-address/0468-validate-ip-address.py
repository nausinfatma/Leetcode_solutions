class Solution:
    def validIPAddress(self, queryIP: str) -> str:

        if '.' in queryIP:
            lst = queryIP.split('.')

            if len(lst) != 4:
                return "Neither"

            for x in lst:
                if not x.isdigit():
                    return "Neither"

                if len(x) > 1 and x[0] == '0':
                    return "Neither"

                if int(x) > 255:
                    return "Neither"

            return "IPv4"

        else:
            lst = queryIP.split(':')

            if len(lst) != 8:
                return "Neither"

            for x in lst:
                if len(x) > 4 or len(x) < 1:
                    return "Neither"

                for y in x:
                    if y not in '0123456789abcdefABCDEF':
                        return "Neither"

            return "IPv6"
                        

        return "Neither"

