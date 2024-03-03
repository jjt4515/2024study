#include <iostream>
#include <vector>
#include <algorithm>
#include <string.h>
#define INF 1000000000;

using namespace std;

// 재귀
int dp[501][501];
int file[501];
int sum[501];

int recursion(int start, int end){
    if(start == end) return dp[start][end] = 0;

    if(dp[start][end] != 0x3f3f3f3f) return dp[start][end];

    if(start + 1 == end) return dp[start][end] = file[start] + file[end];

    for(int mid = start; mid < end; mid++){
        int left = recursion(start, mid);
        int right = recursion(mid + 1, right);
        dp[start][end] = min(dp[start][end], left + right);
    }

    return dp[start][end] += sum[end] - sum[start - 1];
}

int main(){
    int n, tc;
    cin >> tc;

    for(int i = 0; i < tc; i++){
        cin >> n;
        memset(dp, 0x3f, sizeof(dp));
        for(int j = 1; j <= n; j++){
            cin >> file[j];
            sum[j] = sum[j - 1] + file[j];
        }
        cout << recursion(1, n);
    }
    return 0;
}
/* 재귀 x
int main(){
    vector < vector <int> > dp(501,vector <int>(501,0));
    vector<int> file(501, 0);
    vector<int> sum(501, 0);
    int n, tc;
    cin >> tc;

    for(int i = 0; i < tc; i++){
        cin >> n;

        for(int i = 1; i <= n; i++){
            cin >> file[i];
            sum[i] = sum[i - 1] + file[i];
        }

        for(int i = 1; i <= n; i++){
            for(int j = 1; j <= n - i; j++){
                dp[j][i + j] = INF;
                for(int k = j; k < i + j; k++)
                    dp[j][i + j] = min(dp[j][i + j], dp[j][k] + dp[k + 1][i + j] + sum[i + j] - sum[j - 1]);
            }
        }
        cout << dp[1][n] << endl;
    }


    return 0;
}
*/
