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

    for(int player = 0; player < N; player++)
        for (int battle = 2 * card[player]; battle < MAX; battle += card[player]) 
            if (chk[battle]) { 
                scores[card[player]]++;
                scores[battle]--;
            }
    
    for(int i = 0; i < N; i++)
        cout << scores[card[i]] << " ";

    return 0;
}
