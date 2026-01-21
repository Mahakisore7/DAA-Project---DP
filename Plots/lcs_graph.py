import time
import random
import string
import sys
import csv  # Added to generate the Excel file

sys.setrecursionlimit(10**6)

# --- 1. Brute Force (Recursion) ---
def lcs_brute_force(str1, str2):
    if not str1 or not str2:
        return 0
    if str1[-1] == str2[-1]:
        return 1 + lcs_brute_force(str1[:-1], str2[:-1])
    else:
        return max(lcs_brute_force(str1[:-1], str2), 
                   lcs_brute_force(str1, str2[:-1]))

# --- 2. Optimized (DP Tabulation) ---
def lcs_optimized(str1, str2):
    n = len(str1)
    m = len(str2)
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[n][m]

# --- 3. Generator ---
def generate_random_string(length):
    return ''.join(random.choices(string.ascii_uppercase, k=length))

# --- 4. Main Execution & Excel Export ---
def run_analysis():
    print("Running benchmarks... Please wait (this may take 10-20 seconds).")
    
    # We test lengths 2 to 15. 
    # Warning: Going above 15 will make the Brute Force take HUGE amounts of time.
    test_lengths = [2, 4, 6, 8, 10, 11, 12, 13, 14, 15] 
    
    # Prepare data for CSV
    data_rows = []
    
    for n in test_lengths:
        s1 = generate_random_string(n)
        s2 = generate_random_string(n)

        # Measure Brute Force
        start = time.perf_counter()
        lcs_brute_force(s1, s2)
        end = time.perf_counter()
        time_brute = end - start

        # Measure Optimized
        start = time.perf_counter()
        lcs_optimized(s1, s2)
        end = time.perf_counter()
        time_opt = end - start
        
        # Add to list
        data_rows.append([n, time_brute, time_opt])
        print(f"Processed Length {n}: Brute Force={time_brute:.5f}s, DP={time_opt:.5f}s")

    # Write to CSV (Excel compatible file)
    filename = "lcs_runtime_data.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Header Row
        writer.writerow(["Input Size (N)", "Brute Force Time (s)", "Optimized DP Time (s)"])
        # Data Rows
        writer.writerows(data_rows)
        
    print(f"\n[SUCCESS] Data saved to '{filename}'. Open this file in Excel to create your plot.")

if __name__ == "__main__":
    run_analysis()