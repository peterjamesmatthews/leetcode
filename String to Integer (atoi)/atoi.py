class Solution:
    DIGITS = set(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])

    def myAtoi(self, s: str) -> int:
        i = 0  # index of char under consideration

        # ignore leading whitespace
        while i < len(s) and s[i] == " ":
            i += 1

        # determine sign
        sign = 1
        if i < len(s) and s[i] == "+":
            i += 1
        elif i < len(s) and s[i] == "-":
            sign = -1
            i += 1

        val = 0
        while i < len(s) and s[i] in Solution.DIGITS:
            val *= 10
            val += int(s[i])
            i += 1

        # apply sign
        val = sign * val

        # clamp in [-2**31, 2**31 - 1]
        val = min(max(val, -(2**31)), 2**31 - 1)

        return val
