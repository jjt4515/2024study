#include <iostream>
#include <vector>
#define MAX 1000001

using namespace std;


int main()
{
    int N, num;
    cin >> N;

    vector<int> scores(MAX, 0);
    vector<int> chk(MAX, 0);
    vector<int> card;

    for (int i = 0; i < N; i++) {
        cin >> num;
        card.push_back(num);
        chk[num] = 1;
    }

    for(int i = 0; i < N; i++)
        for (int j = 2 * card[i]; j < MAX; j += card[i]) 
            if (chk[j] == 1) { 
                scores[card[i]]++;
                scores[j]--;
            }
    
    for(int i = 0; i < N; i++)
        cout << scores[card[i]] << " ";

    return 0;
}
