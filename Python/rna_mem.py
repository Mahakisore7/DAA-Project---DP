def can_pair(b1, b2):
    pairs = {('A', 'U'), ('U', 'A'), ('C', 'G'), ('G', 'C')}
    return (b1, b2) in pairs

def solve_memoization(rna, i, j, memo):
    
    if i >= j - 4:
        return 0
    

    if (i, j) in memo:
        return memo[(i, j)]
    
    # Option A: j is unpaired
    res = solve_memoization(rna, i, j - 1, memo)
    
    # Option B: j paired with t
    for t in range(i, j - 4):
        if can_pair(rna[t], rna[j]):
            current_option = 1 + solve_memoization(rna, i, t - 1, memo) + \
                                 solve_memoization(rna, t + 1, j - 1, memo)
            res = max(res, current_option)
            
    
    memo[(i, j)] = res
    return res


rna_seq = "ACCGGUAGU"
n = len(rna_seq)
memo_table = {} 

print(f"Sequence: {rna_seq}")
print(f"Max Pairs (Memoization): {solve_memoization(rna_seq, 0, n - 1, memo_table)}")