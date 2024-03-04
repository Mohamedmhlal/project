class Solution:
    def solve(self, A, B):
        l = 0
        max_length = 0
        zeros_count = 0

        for r in range(len(A)):
            if A[r] == 0:
                zeros_count += 1

            while zeros_count > B:
                if A[l] == 0:
                    zeros_count -= 1
                l += 1

            max_length = max(max_length, r - l + 1)

        return max_length