// Longest Common Subsequence - Tabulation Approach
#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;

int lcsTab(string str1 , string str2 ){
    if(str1.size()==0 || str2.size()==0){
        return 0;
    }

    int n = str1.size();
    int m = str2.size();

    vector<vector<int>>dp(n+1,vector<int>(m+1,0));

    for(int i=1;i<=n;i++){
        for(int j=1;j<=m;j++){
            if(str1[i-1] == str2[j-1]){
                dp[i][j] = 1 + dp[i-1][j-1];
            }
            else {
                dp[i][j] = max(dp[i-1][j],dp[i][j-1]);
            }
        }
    }



    return dp[n][m];
}

int main(){
    string str1 = "abcd";
    string str2 = "abcd";
    int n = str1.size();
    int m = str2.size();

    
    cout<< lcsTab(str1 , str2 ) << endl;
    return 0;

}