#include <iostream>
#include <vector>
#include <stack>

using namespace std;

int main(void){
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    int testCase;

    cin>>testCase;

    for(int i=0;i<testCase;i++){
        int m,n,k;
        cin>>m>>n>>k;
        int answer=0;
        vector<vector<int>> field;
        vector<int> v(m,0);
        for(int j=0;j<n;j++){
            field.push_back(v);
        } //밭 만들기. 초기 상태는 0으로 초기화
        vector<pair<int,int>> positions; 
        for(int j=0;j<k;j++){
            int pos_x,pos_y;
            cin>>pos_x>>pos_y;
            field[pos_y][pos_x]=1; // 밭에 배추 심기. 
            positions.push_back(make_pair(pos_y,pos_x)); //위치 기억해서 바로 시작
        }

        for(auto position : positions){
            stack<pair<int,int>> s; //dfs

            if(field[position.first][position.second]!=1){ //2인 경우
                continue;
            }else{ //1인 경우
                answer++;
                s.push(position);
                int dx[4]={-1,0,1,0};
                int dy[4]={0,1,0,-1};
                while(!s.empty()){
                    int pos_x = s.top().first;
                    int pos_y = s.top().second;
                    s.pop();
                    field[pos_x][pos_y]=2;
                    // 다음 땅이 배추가 심어져 있지 않거나, 배추를 심고 방문한 땅이라면
                    for(int j=0;j<4;j++){
                        int next_pos_x = pos_x + dx[j];
                        int next_pos_y = pos_y + dy[j];
                        //범위 내에 있으면서 
                        if(next_pos_x>=0 && next_pos_x<=n-1 && next_pos_y>=0 && next_pos_y<=m-1){
                            if(field[next_pos_x][next_pos_y]==1){
                                s.push(make_pair(next_pos_x,next_pos_y));
                            }
                        }
                    }
                }
            }

        }
        cout<<answer<<endl;
    }
    return 0;
}
