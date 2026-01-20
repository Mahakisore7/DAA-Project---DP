#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

// Global DP table to make it easy to access in recursion
vector<vector<int>> dp;
string rna;

bool canPair(char base1, char base2) {
    if (base1 == 'A' && base2 == 'U') return true;
    if (base1 == 'U' && base2 == 'A') return true;
    if (base1 == 'C' && base2 == 'G') return true;
    if (base1 == 'G' && base2 == 'C') return true;
    return false;
}

// 1. THE SOLVER (Fills the table)
void optimizeRNA() {
    int n = rna.length();
    // Resize table to n x n and fill with 0
    dp.assign(n, vector<int>(n, 0));

    // Length k from 5 to n
    for (int k = 5; k < n; k++) {
        for (int i = 0; i < n - k; i++) {
            int j = i + k;
            
            // Option A: j unpaired
            dp[i][j] = dp[i][j-1];

            // Option B: j paired with t
            for (int t = i; t <= j - 5; t++) {
                if (canPair(rna[t], rna[j])) {
                    int valInside = dp[t+1][j-1];
                    int valOutside = (t > i) ? dp[i][t-1] : 0;
                    
                    int currentPairVal = 1 + valInside + valOutside;
                    
                    if (currentPairVal > dp[i][j]) {
                        dp[i][j] = currentPairVal;
                    }
                }
            }
        }
    }
}

// 2. THE BACKTRACKER (Finds the pairs)
void backtrack(int i, int j) {
    // Base case: If segment is too small, no pairs exist here.
    if (i >= j - 4) {
        return;
    }

    // Check Option A: Did we skip j?
    // If the score is the same as excluding j, then j was definitely skipped.
    if (dp[i][j] == dp[i][j-1]) {
        backtrack(i, j - 1);
        return;
    }

    // Check Option B: j was paired. Find with whom (t).
    for (int t = i; t <= j - 5; t++) {
        if (canPair(rna[t], rna[j])) {
            int valInside = dp[t+1][j-1];
            int valOutside = (t > i) ? dp[i][t-1] : 0;

            // Re-calculate to see if this t was the one we chose
            if (dp[i][j] == 1 + valInside + valOutside) {
                // FOUND IT!
                cout << "Pair found: Index " << t << " (" << rna[t] 
                     << ") - Index " << j << " (" << rna[j] << ")" << endl;
                
                // Recurse into the two split parts
                backtrack(i, t - 1);   // The outside part
                backtrack(t + 1, j - 1); // The inside part
                return; // We found the pair, so we stop checking other t's
            }
        }
    }
}

int main() {
    // Test Sequence from our manual trace
    rna = "ACCGGUAGU"; 
    
    cout << "Analyzing RNA: " << rna << endl;
    
    // Step 1: Fill the table
    optimizeRNA();
    int n = rna.length();

    cout << "Max Pairs: " << dp[0][n-1] << endl;
    
    // Step 2: Reconstruct solution
    cout << "Structure Details:" << endl;
    backtrack(0, n - 1);

    return 0;
}