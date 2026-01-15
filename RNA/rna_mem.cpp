#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cstring> // for memset

using namespace std;

string rna;
// 1. THE NOTEBOOK
// We make a table large enough for the string size.
// memo[i][j] stores the result for interval i to j.
int memo[1000][1000]; 

bool canPair(char base1, char base2) {
    if (base1 == 'A' && base2 == 'U') return true;
    if (base1 == 'U' && base2 == 'A') return true;
    if (base1 == 'C' && base2 == 'G') return true;
    if (base1 == 'G' && base2 == 'C') return true;
    return false;
}

int solve(int i, int j) {
    // Base Case: Too short for a sharp turn?
    if (i >= j - 4) {
        return 0;
    }

    // 2. CHECK THE NOTEBOOK
    // If we already wrote an answer here (value is not -1), return it immediately.
    if (memo[i][j] != -1) {
        return memo[i][j];
    }

    // --- The Logic is exactly the same as Brute Force ---
    
    // Option A: j is unpaired
    int res = solve(i, j - 1);

    // Option B: j pairs with t
    for (int t = i; t <= j - 5; t++) {
        if (canPair(rna[t], rna[j])) {
            int currentOption = 1 + solve(i, t - 1) + solve(t + 1, j - 1);
            res = max(res, currentOption);
        }
    }

    // 3. WRITE IN THE NOTEBOOK
    // Save the result before leaving so we never calculate this (i, j) again.
    memo[i][j] = res;
    
    return res;
}

int main() {
    rna = "ACCGGUAGU"; 
    int n = rna.length();

    // Initialize the notebook with -1
    // (This tells the computer "I haven't solved anything yet")
    memset(memo, -1, sizeof(memo));

    cout << "RNA Sequence: " << rna << endl;
    cout << "Maximum Base Pairs: " << solve(0, n - 1) << endl;

    return 0;
}