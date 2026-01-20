#include <iostream>
#include <string>
#include <algorithm> 
#include <vector>

using namespace std;

string rna;

// Helper function to check if two bases can pair
// Watson-Crick: A-U and C-G
bool canPair(char base1, char base2) {
    if (base1 == 'A' && base2 == 'U') return true;
    if (base1 == 'U' && base2 == 'A') return true;
    if (base1 == 'C' && base2 == 'G') return true;
    if (base1 == 'G' && base2 == 'C') return true;
    return false;
}

// Recursive Brute Force Function
// Returns max pairs possible for substring rna[i...j]
int solve(int i, int j) {
    // BASE CASE:
    // If indices cross or if the distance is too small (sharp turn rule).
    // The rule says i < j - 4, so if i >= j - 4, we cannot form any NEW pairs.
    // (Note: In 0-indexed string, distance checks might vary slightly, 
    // but let's stick to the logic: if j - i < 5, return 0).
    if (i >= j - 4) {
        return 0;
    }

    // OPTION 1: j is NOT involved in a pair.
    // The result is just whatever we could get from i to j-1.
    int res = solve(i, j - 1);

    // OPTION 2: j pairs with some t.
    // We try all possible t from i up to j - 5 (to satisfy sharp turn).
    for (int t = i; t <= j - 5; t++) {
        
        // Check if base at t and base at j are compatible
        if (canPair(rna[t], rna[j])) {
            
            // If they pair, we get:
            // 1 (current pair)
            // + best of "outside" (i to t-1
            // + best of "inside" (t+1 to j-1)
            int currentOption = 1 + solve(i, t - 1) + solve(t + 1, j - 1);
            
            // Update our result if this option is better
            res = max(res, currentOption);
        }
    }

    return res;
}

int main() {
    // Example from the text logic
    // Sequence needs to be long enough to satisfy sharp turn (length > 5)
    rna = "ACCGGUAGU"; 
    
    int n = rna.length();
    
    // We want the solution for the whole string (0 to n-1)
    cout << "RNA Sequence: " << rna << endl;
    cout << "Maximum Base Pairs: " << solve(0, n - 1) << endl;

    return 0;
}