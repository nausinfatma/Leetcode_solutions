from math import gcd

class Solution:
    def fractionAddition(self, expression: str) -> str:

        num = 0
        den = 1
        i = 0

        while i < len(expression):

            sign = 1

            if expression[i] == '-':
                sign = -1
                i += 1
            elif expression[i] == '+':
                i += 1

            n_ = 0
            while i < len(expression) and expression[i].isdigit():
                n_ = n_ * 10 + int(expression[i])
                i += 1

            i += 1  # skip /

            d_ = 0
            while i < len(expression) and expression[i].isdigit():
                d_ = d_ * 10 + int(expression[i])
                i += 1

            n_ *= sign

            num = num * d_ + den * n_
            den = den * d_

        g = gcd(abs(num), den)

        num //= g
        den //= g

        return f"{num}/{den}"