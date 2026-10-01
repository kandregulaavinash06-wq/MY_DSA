#approach 1

class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)
        rev = 0
        while x != 0:
            digit = x % 10
            rev = rev * 10 + digit
            x //= 10
        rev *= sign
        if rev < -2147483648 or rev > 2147483647:
            return 0
        return rev

#approach 2

class Solution:
    def reverse(self, x: int) -> int:
        if x<0:
            rev=-int(str(x)[1:][::-1])
        else:
            rev=int(str(x)[::-1])
        return rev if -2147483648<=rev<=2147483647 else 0