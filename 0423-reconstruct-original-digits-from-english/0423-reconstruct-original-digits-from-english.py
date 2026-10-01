from collections import Counter

class Solution:
    def originalDigits(self, s: str) -> str:

        count = Counter(s)
        s = list(s)
        ans = []

        if count['z']:
            ans.append('0' * count['z'])
            x = count['z']

            for ch in "zero":
                count[ch] -= x

        if count['w']:
            ans.append('2' * count['w'])
            x = count['w']

            for ch in "two":
                count[ch] -= x


        if count['u']:
            ans.append('4' * count['u'])
            x = count['u']

            for ch in "four":
                count[ch] -= x


        if count['x']:
            ans.append('6' * count['x'])
            x = count['x']

            for ch in "six":
                count[ch] -= x


        if count['g']:
            ans.append('8' * count['g'])
            x = count['g']

            for ch in "eight":
                count[ch] -= x

        while all(count[x] > 0 for x in 'one'):
            for x in 'one':
                count[x] -= 1
            ans += '1'

        while all(count[x] > 0 for x in 'three'):
            for x in 'three':
                count[x] -= 1
            ans += '3'

        while all(count[x] > 0 for x in 'five'):
            for x in 'five':
                count[x] -= 1
            ans += '5'

        while all(count[x] > 0 for x in 'seven'):
            for x in 'seven':
                count[x] -= 1
            ans += '7'

        while all(count[x] > 0 for x in 'nine'):
            for x in 'nine':
                count[x] -= 1
            ans += '9'

        ans.sort()

        return ''.join(ans)


        