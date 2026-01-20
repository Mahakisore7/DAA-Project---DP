import sys
sys.setrecursionlimit(2000)

def lcs_mem(str1, str2, dp):
    if not str1 or not str2:
        return 0
    
    n = len(str1)
    m = len(str2)
    
    if dp[n][m] != -1:
        return dp[n][m]

    if str1[-1] == str2[-1]:
        dp[n][m] = 1 + lcs_mem(str1[:-1], str2[:-1], dp)
    else:
        ans1 = lcs_mem(str1[:-1], str2, dp)
        ans2 = lcs_mem(str1, str2[:-1], dp)
        dp[n][m] = max(ans1, ans2)
        
    return dp[n][m]

if __name__ == "__main__":
    str1 = "abcd"
    str2 = "abc"
    
    n = len(str1)
    m = len(str2)

    dp = [[-1 for _ in range(m + 1)] for _ in range(n + 1)]
    
    print(lcs_mem(str1, str2, dp))
    print(dp)