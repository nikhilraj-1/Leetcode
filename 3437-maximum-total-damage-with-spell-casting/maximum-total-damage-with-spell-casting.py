class Solution:
    def maximumTotalDamage(self, power):
        from collections import Counter
        cnt = Counter(power)

        vals = [(-10**9, 0)] + sorted(cnt.items())
        n = len(vals)
        dp = [0] * n
        best = 0
        j = 1

        for i in range(1, n):

            while j < i and vals[j][0] < vals[i][0] - 2:
                best = max(best, dp[j])
                j += 1
            dp[i] = best + vals[i][0] * vals[i][1]

        return max(dp)