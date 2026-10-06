class Solution:
    def compress(self, chars: list[str]) -> int:
        cnt = 1
        ch = chars[0]
        write = 0

        for i in range(1, len(chars)):
            if chars[i] == chars[i - 1]:
                cnt += 1

            else:

                chars[write] = ch
                write += 1


                if cnt != 1:
                    for digit in str(cnt):
                        chars[write] = digit
                        write += 1

                cnt = 1
                ch = chars[i]


        chars[write] = ch
        write += 1

        if cnt != 1:
            for digit in str(cnt):
                chars[write] = digit
                write += 1

        return write