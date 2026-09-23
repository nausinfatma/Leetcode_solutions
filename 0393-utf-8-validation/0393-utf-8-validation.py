class Solution:
    def validUtf8(self, data: list[int]) -> bool:
        remaining = 0

        for num in data:
            num &= 0xFF

            if remaining:
                if (num & 0b11000000) != 0b10000000:
                    return False
                remaining -= 1

            elif (num & 0b10000000) == 0:
                remaining = 0

            elif (num & 0b11100000) == 0b11000000:
                remaining = 1

            elif (num & 0b11110000) == 0b11100000:
                remaining = 2

            elif (num & 0b11111000) == 0b11110000:
                remaining = 3

            else:
                return False

        return remaining == 0