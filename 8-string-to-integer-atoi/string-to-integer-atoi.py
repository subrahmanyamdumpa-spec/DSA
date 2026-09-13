class Solution:
    def myAtoi(self, s):
        i = 0
        sign = 1
        num = 0
        n = len(s)

        while i < n and s[i] == " ":
            i += 1

        if i < n and (s[i] == "+" or s[i] == "-"):
            if s[i] == "-":
                sign = -1
            i += 1

        while i < n and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1

        result = sign * num

        if result < -2147483648:
            return -2147483648
        if result > 2147483647:
            return 2147483647

        return result
        