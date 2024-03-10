#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int cnt, start, end, result = 0;
    cin >> cnt;

    vector<int> vec(cnt);

    for(int i = 0; i < cnt; i++)    
        cin >> vec[i];
    
    sort(vec.begin(), vec.end());

    for(int i = 0; i < cnt; i++){
        start = 0;
        end = cnt - 1;
        int sum, target = vec[i];
        
        while(start < end){
            sum = vec[start] + vec[end];
            if(target == sum){ 
                if(start != i && end != i){
                    result++;
                    break;
                }
                else if(start == i) start++;
                else if(end == i) end--;
            }
            else if(target < sum) end--;
            else if(target > sum) start++;
        }   
    }

    cout << result;
    return 0;
}
