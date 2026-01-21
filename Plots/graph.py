import time
import random
import sys

# Increase recursion depth for brute force
sys.setrecursionlimit(5000)

# ==========================================
# 1. LCS ALGORITHMS
# ==========================================
def lcs_brute_force(X, Y, m, n):
    if m == 0 or n == 0:
        return 0
    if X[m-1] == Y[n-1]:
        return 1 + lcs_brute_force(X, Y, m-1, n-1)
    else:
        return max(lcs_brute_force(X, Y, m, n-1), lcs_brute_force(X, Y, m-1, n))

def lcs_dp(X, Y):
    m, n = len(X), len(Y)
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]

# ==========================================
# 2. RNA ALGORITHMS
# ==========================================
def rna_brute_force(s, i, j):
    if i >= j - 4: return 0
    res = rna_brute_force(s, i, j - 1)
    for t in range(i, j - 4):
        # Simplified pair check for benchmarking speed
        # (Assuming A-U, C-G)
        if (s[t]=='A' and s[j]=='U') or (s[t]=='U' and s[j]=='A') or \
           (s[t]=='C' and s[j]=='G') or (s[t]=='G' and s[j]=='C'):
            res = max(res, 1 + rna_brute_force(s, i, t - 1) + rna_brute_force(s, t + 1, j - 1))
    return res

def rna_dp(s):
    n = len(s)
    dp = [[0]*n for _ in range(n)]
    for k in range(5, n):
        for i in range(n - k):
            j = i + k
            dp[i][j] = dp[i][j-1]
            for t in range(i, j - 4):
                if (s[t]=='A' and s[j]=='U') or (s[t]=='U' and s[j]=='A') or \
                   (s[t]=='C' and s[j]=='G') or (s[t]=='G' and s[j]=='C'):
                    inside = dp[t+1][j-1]
                    outside = dp[i][t-1] if t > i else 0
                    if 1 + inside + outside > dp[i][j]:
                        dp[i][j] = 1 + inside + outside
    return dp[0][n-1]

# ==========================================
# 3. GENERATE EXCEL DATA
# ==========================================
def run_benchmark():
    print("Copy the data below into Excel to create your charts:\n")
    print(f"{'Input_Size':<12} | {'LCS_Brute':<12} | {'LCS_DP':<12} | {'RNA_Brute':<12} | {'RNA_DP':<12}")
    print("-" * 70)

    # Test sizes. 
    # NOTE: RNA Brute Force is VERY slow. We stop brute force early.
    sizes = [5, 10, 12, 15, 18, 20] 

    for n in sizes:
        # Generate random inputs
        str1 = "".join(random.choices("ACGU", k=n))
        str2 = "".join(random.choices("ACGU", k=n))

        # --- LCS Timing ---
        # Brute
        start = time.time()
        lcs_brute_force(str1, str2, n, n)
        lcs_bf_time = time.time() - start
        
        # DP
        start = time.time()
        lcs_dp(str1, str2)
        lcs_dp_time = time.time() - start

        # --- RNA Timing ---
        # Brute
        start = time.time()
        rna_brute_force(str1, 0, n-1)
        rna_bf_time = time.time() - start
        
        # DP
        start = time.time()
        rna_dp(str1)
        rna_dp_time = time.time() - start

        print(f"{n:<12} | {lcs_bf_time:<12.6f} | {lcs_dp_time:<12.6f} | {rna_bf_time:<12.6f} | {rna_dp_time:<12.6f}")

if __name__ == "__main__":
    run_benchmark()