#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

bool canPair(char base1, char base2) {
    if (base1 == 'A' && base2 == 'U') return true;
    if (base1 == 'U' && base2 == 'A') return true;
    if (base1 == 'C' && base2 == 'G') return true;
    if (base1 == 'G' && base2 == 'C') return true;
    return false;
}

int optimizeRNA(string rna) {
    int n = rna.length();
    
    // DP Table: dp[i][j] stores max pairs for interval i...j
    // We initialize everything to 0.
    vector<vector<int>> dp(n, vector<int>(n, 0));

    // OUTER LOOP: Length of the interval (k)
    // We start from 5 because any interval < 5 has 0 pairs (sharp turn rule).
    // In the PDF, k is used as the difference (j - i).
    for (int k = 5; k < n; k++) {
        
        // INNER LOOP: Start position (i)
        // We slide the window of length 'k' across the string.
        for (int i = 0; i < n - k; i++) {
            
            int j = i + k; // End position is start + length
            
            // LOGIC: Same as before!
            
            // 1. Option A: j is unpaired (take result from i...j-1)
            dp[i][j] = dp[i][j-1];

            // 2. Option B: Try to pair j with some t
            // t must be between i and j-5 (inclusive)
            for (int t = i; t <= j - 5; t++) {
                
                if (canPair(rna[t], rna[j])) {
                    // 1 pair + inside (t+1...j-1) + outside (i...t-1)
                    // Note: We need to be careful not to access negative indices for outside part
                    int valInside = dp[t+1][j-1];
                    int valOutside = (t > i) ? dp[i][t-1] : 0; // if t==i, outside is empty
                    
                    int currentOption = 1 + valInside + valOutside;
                    
                    dp[i][j] = max(dp[i][j], currentOption);
                }
            }
        }
    }
    
    // The answer for the whole string is at dp[0][n-1]
    return dp[0][n-1];
}

int main() {
    string rna = "ACCGGUAGU";
    cout << "RNA Sequence: " << rna << endl;
    cout << "Maximum Base Pairs: " << optimizeRNA(rna) << endl;
    return 0;
}