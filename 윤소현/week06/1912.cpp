#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(void){
    int n;
    cin >> n;
    vector<int>vec(n);
    vector<int>dp(n);

    for(int i = 0; i < n; i++)
        cin >> vec[i];

    dp[0] = vec[0];
    for(int i = 1; i < n; i++)
        dp[i] = max(vec[i], dp[i-1] + vec[i]);

    cout << *max_element(dp.begin(), dp.end());

    return 0;
}
