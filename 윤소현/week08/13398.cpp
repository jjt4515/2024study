#include <iostream>

using namespace std;
int dp[100001][2], arr[100001];

int main(void) {
    int n;
    cin >> n;
    for(int i = 0; i < n; i++)
        cin >> arr[i];

    dp[0][0] = arr[0];
	dp[0][1] = arr[0];
	int result = arr[0];

    for (int i = 1; i < n; i++)
	{
		dp[i][0] = max(dp[i - 1][0] + arr[i], arr[i]);
		dp[i][1] = max(dp[i - 1][0], dp[i - 1][1] + arr[i]);
		result = max(result, max(dp[i][0], dp[i][1]));
	}
	cout << result;

    return 0;
}
