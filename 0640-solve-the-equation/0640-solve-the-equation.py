class Solution:
    def solveEquation(self, equation: str) -> str:
        left, right = equation.split('=')

        def evaluate(expr):
            x_coeff = 0
            constant = 0

            expr = expr.replace('-', '+-')
            terms = expr.split('+')

            for term in terms:
                if not term:
                    continue

                if 'x' in term:
                    coeff = term.replace('x', '')

                    if coeff == '' or coeff == '+':
                        x_coeff += 1
                    elif coeff == '-':
                        x_coeff -= 1
                    else:
                        x_coeff += int(coeff)
                else:
                    constant += int(term)

            return x_coeff, constant

        a, b = evaluate(left)
        c, d = evaluate(right)

        coeff = a - c
        const = d - b

        if coeff == 0:
            if const == 0:
                return "Infinite solutions"
            else:
                return "No solution"

        x = const // coeff
        return f"x={x}"