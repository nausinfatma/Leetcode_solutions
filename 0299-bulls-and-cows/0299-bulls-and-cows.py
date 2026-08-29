class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        a = 0
        b = 0
        secret = list(secret)
        guess = list(guess)

        for i in range(len(secret)):
            if secret[i] == guess[i]:
                a += 1
                secret[i] = '#'
                guess[i] = '#'

        secret.sort()
        guess.sort()

        for i in range(len(secret)):
            if secret[i] != '#' and secret[i] in guess:
                j = guess.index(secret[i])
                b += 1
                guess[j] = '#'


        return f"{a}A{b}B"
