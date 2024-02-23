#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int total, cnt;
int parents[101];
vector<pair<int, pair<int, int> > > lan;

bool cmp(pair<int, pair<int, int> > x, pair<int, pair<int, int> > y) { return x.first < y.first; }

int unionFind(int x){
    if(parents[x] == x) return x;
    else return parents[x] = unionFind(parents[x]);
}

void merge(int x, int y) {
    x = unionFind(x);
    y = unionFind(y);
    
    if(x > y) parents[x] = y;
    else parents[y] = x;
}

void mst(){
    for(int i = 1; i < cnt; i++)
        parents[i] = i;
    sort(lan.begin(), lan.end(), cmp);

    for(int i = 0; i < lan.size(); i++){
        int node1 = lan[i].second.first;
        int node2 = lan[i].second.second;
        int cost = lan[i].first;

        if(unionFind(node1) != unionFind(node2)){
            merge(node1, node2);
            total -= cost;
        }
    }

    int tmp = unionFind(1);
    for(int i = 2; i <= cnt; i++)
        if(unionFind(i) != tmp){
            cout << -1 << endl;
            return;
        }
    cout << total;
}

int main(void){
    int cost;
    char c;
    cin >> cnt;

    for(int i = 1; i <= cnt; i++)
        for(int j = 1; j <= cnt; j++){
            cin >> c;
            
            if(c >= 'a' && c <= 'z'){
                cost = c - 'a' + 1;
                lan.push_back({cost, {i, j}});
                total += cost;
            }
            else if(c >= 'A' && c <= 'Z'){
                cost = c - 'A' + 27;
                lan.push_back({cost, {i, j}});
                total += cost;
            }
        }
    
    mst();

    return 0;
}
