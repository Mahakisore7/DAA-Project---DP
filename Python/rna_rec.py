def can_pair(b1, b2):
    pairs = {('A', 'U'), ('U', 'A'), ('C', 'G'), ('G', 'C')}
    return (b1, b2) in pairs

def solve_brute_force(rna, i, j):
    if i >= j - 4:
        return 0
    
    # Option A: j is NOT paired.
    # We simply skip j and solve for i to j-1.
    res = solve_brute_force(rna, i, j - 1)
    
    # Option B: j IS paired with some t.
    # Try all possible t from i up to j-5.
    for t in range(i, j - 4):
        if can_pair(rna[t], rna[j]):
            # 1 pair + Max pairs inside the arc + Max pairs outside the arc
            # The "inside" is t+1...j-1
            # The "outside" is i...t-1
            current_option = 1 + solve_brute_force(rna, i, t - 1) + \
                                 solve_brute_force(rna, t + 1, j - 1)
            
            res = max(res, current_option)
            
    return res

rna_seq = "ACCGGUAGU"
n = len(rna_seq)
print(f"Sequence: {rna_seq}")
print(f"Max Pairs (Brute Force): {solve_brute_force(rna_seq, 0, n - 1)}")