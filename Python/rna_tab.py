def solve_tabulation(rna):
    n = len(rna)
   
    dp = [[0 for _ in range(n)] for _ in range(n)]
    
    def can_pair(b1, b2):
        pairs = {('A', 'U'), ('U', 'A'), ('C', 'G'), ('G', 'C')}
        return (b1, b2) in pairs

    # OUTER LOOP: Length of interval 'k'
    # Start at 5 because sharp turns (len < 5) allow 0 pairs.
    for k in range(5, n):
        
        # INNER LOOP: Start position 'i'
        for i in range(n - k):
            j = i + k # End position
            
            # Option A: j is unpaired (take value from left neighbor)
            dp[i][j] = dp[i][j-1]  
            
            # Option B: Try to pair j with t
            for t in range(i, j - 4):
                if can_pair(rna[t], rna[j]):
                    # Get values from the table. 
                    # Be careful with indices: if t==i, 'outside' is empty (0)
                    inside = dp[t+1][j-1]
                    outside = dp[i][t-1] if t > i else 0
                    
                    current_val = 1 + inside + outside
                    
                    if current_val > dp[i][j]:
                        dp[i][j] = current_val
                        
    # The answer for the full string (0 to n-1) is in the top-right corner
    return dp[0][n-1]


rna_seq = "ACCGGUAGU"
print(f"Sequence: {rna_seq}")
print(f"Max Pairs (Tabulation): {solve_tabulation(rna_seq)}")