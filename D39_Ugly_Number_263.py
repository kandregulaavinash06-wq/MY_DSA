class Solution:
    def isUgly(self, n: int) -> bool:
        # Ugly numbers must be positive
        if n <= 0:
            return False

        # Keep removing factors of 2, 3, and 5
        while n:
            if n == 1:
                return True

            if n % 3 == 0:
                n //= 3
            elif n % 2 == 0:
                n //= 2
            elif n % 5 == 0:
                n //= 5
            else:
                # A remaining factor other than 2, 3, or 5
                return False