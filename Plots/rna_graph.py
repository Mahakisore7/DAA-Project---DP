import time
import random
import sys
import csv

# Increase recursion limit for deep recursion trees
sys.setrecursionlimit(10**6)

# ==========================================
# PART 1: Helper Functions
# ==========================================
def can_pair(b1, b2):
    pairs = {('A', 'U'), ('U', 'A'), ('C', 'G'), ('G', 'C')}
    return (b1, b2) in pairs

def generate_rna_string(length):
    return ''.join(random.choices(['A', 'C', 'G', 'U'], k=length))

# ==========================================
# PART 2: Brute Force (Recursion)
# Time Complexity: O(2^n) - Exponential
# ==========================================
def solve_brute_force(rna, i, j):
    # Constraint: No sharp turns (must have >4 bases between i and j)
    if i >= j - 4:
        return 0
    
    # Option A: j is NOT paired.
    res = solve_brute_force(rna, i, j - 1)
    
    # Option B: j IS paired with some t.
    for t in range(i, j - 4):
        if can_pair(rna[t], rna[j]):
            # 1 (the pair t,j) + max inside (t+1...j-1) + max outside (i...t-1)
            current_option = 1 + solve_brute_force(rna, i, t - 1) + \
                                 solve_brute_force(rna, t + 1, j - 1)
            res = max(res, current_option)
            
    return res

# ==========================================
# PART 3: Optimized Solution (DP Tabulation)
# Time Complexity: O(n^3) - Polynomial
# ==========================================
def solve_tabulation(rna):
    n = len(rna)
    dp = [[0 for _ in range(n)] for _ in range(n)]

    # k is the length of the interval (j - i)
    # We start from 5 because intervals < 5 cannot have pairs (sharp turns)
    for k in range(5, n):
        for i in range(n - k):
            j = i + k
            
            # Option A: j is unpaired
            dp[i][j] = dp[i][j-1]
            
            # Option B: j pairs with t
            for t in range(i, j - 4):
                if can_pair(rna[t], rna[j]):
                    inside = dp[t+1][j-1]
                    # Check boundary condition for outside
                    outside = dp[i][t-1] if t > i else 0
                    
                    if 1 + inside + outside > dp[i][j]:
                        dp[i][j] = 1 + inside + outside
                        
    return dp[0][n-1]

# ==========================================
# PART 4: Execution & Visualization Data
# ==========================================
def run_analysis():
    print("================================================================")
    print("       RNA PREDICTION PERFORMANCE ANALYSIS                      ")
    print("================================================================")
    print("Running benchmarks... (This may take a moment)")
    
    # Data container for CSV
    results = []
    
    # We test small lengths because RNA Brute Force is extremely slow (O(2^n))
    # Note: Even n=20 might take too long for Brute Force on some machines.
    test_lengths = [6, 8, 10, 12, 14, 16, 18]

    for n in test_lengths:
        seq = generate_rna_string(n)
        
        # 1. Measure Brute Force
        start = time.perf_counter()
        solve_brute_force(seq, 0, n - 1)
        end = time.perf_counter()
        time_brute = end - start
        
        # 2. Measure Optimized DP
        start = time.perf_counter()
        solve_tabulation(seq)
        end = time.perf_counter()
        time_dp = end - start
        
        results.append([n, time_brute, time_dp])
        print(f"Length {n}: Brute Force = {time_brute:.5f}s | DP = {time_dp:.5f}s")

    # Save to CSV for Excel
    filename = "rna_runtime_data.csv"
    with open(filename, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Input Size (n)", "Brute Force (s)", "Optimized DP (s)"])
        writer.writerows(results)
        
    print(f"\n[SUCCESS] Data saved to '{filename}'. Open in Excel to create plots.")

if __name__ == "__main__":
    run_analysis()