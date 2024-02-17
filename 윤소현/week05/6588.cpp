#include <iostream>
#include <vector>
#include <math.h>
#define MAX 1000000

using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    int n;
    cin >> n;

    vector<int> vec(MAX, 1);
    vec[0] = vec[1] = 0;

    for(int i = 2; i <= sqrt(MAX); i++)
        if(vec[i] == 1)
            for(int j = 2; i * j < MAX; j++)
                vec[i * j] = 0;
    
    while(n != 0){
        bool chk = false;
        for(int i = 3; i < n; i += 2)
            if(vec[i] && vec[n - i]) { 
                cout << n << " = " << i << " + " << n- i << "\n";
                chk = true;
                break;
            }

        if(!chk)   
            cout << "Goldbach's conjecture is wrong.\n";

        cin >> n;
    }
    return 0;
}
