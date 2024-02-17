#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<char> ans;
vector<char> pw;

int L, C;
char ch;
bool count(){
    int v, c;
    v = c = 0;

    for(int i = 0; i < L; i++)
        if(ans[i] == 'a' || ans[i] == 'e' || ans[i] == 'i' || ans[i] == 'o' || ans[i] == 'u')
            v++;
        else
            c++;
    if(v >= 1 && c >=2) return true;
    return false;
    
}
void backTracking(int n){
    if(ans.size() == L)
        if(count()){
            for(char a : ans)
                cout << a;
            cout << "\n";
        }

    for(int i = n; i < C; i++){
        ans.push_back(pw[i]);
        backTracking(i + 1);
        ans.pop_back();
    }
}

int main(){
    cin >> L >> C;
    for(int i = 0; i < C; i++){
        cin >> ch;
        pw.push_back(ch);
    }
    
    sort(pw.begin(), pw.end());
    
    backTracking(0);

    return 0;
}
