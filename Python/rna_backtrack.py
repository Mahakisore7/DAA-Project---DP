def can_pair(b1, b2):
    pairs = {('A', 'U'), ('U', 'A'), ('C', 'G'), ('G', 'C')}
    return (b1, b2) in pairs

def get_rna_structure(rna):
    n = len(rna)
    dp = [[0 for _ in range(n)] for _ in range(n)]

    # --- STEP 1: Fill the Table (Tabulation) ---
    for k in range(5, n):
        for i in range(n - k):
            j = i + k
            dp[i][j] = dp[i][j-1]
            
            for t in range(i, j - 4):
                if can_pair(rna[t], rna[j]):
                    inside = dp[t+1][j-1]
                    outside = dp[i][t-1] if t > i else 0
                    if 1 + inside + outside > dp[i][j]:
                        dp[i][j] = 1 + inside + outside

    # --- STEP 2: Backtracking Function ---
    def backtrack(i, j):
        # Base Case: Interval too small for any pairs
        if i >= j - 4:
            return

        # Check Option A: Did we skip j?
        # If score is same as (i, j-1), then j was definitely skipped.
        if dp[i][j] == dp[i][j-1]:
            backtrack(i, j - 1)
            return

        # Check Option B: j was paired. Find with whom (t).
        for t in range(i, j - 4):
            if can_pair(rna[t], rna[j]):
                inside = dp[t+1][j-1]
                outside = dp[i][t-1] if t > i else 0
                
                # Check if this t creates the winning score
                if dp[i][j] == 1 + inside + outside:
                    print(f"Pair found: Index {t} ({rna[t]}) - Index {j} ({rna[j]})")
                    
                    # Recursively solve the two split parts
                    backtrack(i, t - 1)    # Outside
                    backtrack(t + 1, j - 1) # Inside
                    return # Stop after finding the correct pair

    # Print Results
    print(f"Total Max Pairs: {dp[0][n-1]}")
    print("Structure Details:")
    backtrack(0, n - 1)

# --- Main Execution ---
rna_seq = "ACCGGUAGU"
print(f"Sequence: {rna_seq}")
get_rna_structure(rna_seq)