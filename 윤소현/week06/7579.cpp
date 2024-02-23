#include <iostream>

using namespace std;

int dp[101][10001];

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N, M, num, cost = 0;
    cin >> N >> M;

    int m[101];
    int c[101];

    for(int i = 1; i <= N; i++) cin >> m[i];
    for(int i = 1; i <= N; i++) {
        cin >> c[i];
        cost += c[i];
    }

    for(int i = 1; i <= N; i++)
        for(int j = 0; j <= cost; j++){
            if(c[i] > j)  
                dp[i][j] = dp[i-1][j];
            else{
                dp[i][j] = max(m[i] + dp[i-1][j - c[i]], dp[i-1][j]);
            }
        }
    
    for(int i = 0; i <= cost; i++)
        if(dp[N][i] >= M){
            cout << i << endl;
            break;
        }

    return 0;
}
