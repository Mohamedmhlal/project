class Solution:
    def is_prime(self, n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def primesum(self, A):
        for i in range(2, A):
            if self.is_prime(i) and self.is_prime(A - i):
                return [i, A - i]