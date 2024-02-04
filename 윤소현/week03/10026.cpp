//
// Created by SoHyeon on 2024/01/28.
//
#include <iostream>
#include <queue>
#define MAX 101

using namespace std;
int n;
char map[MAX][MAX];
int dx[4] = {1, -1, 0 , 0};
int dy[4] = {0, 0, 1, -1};
bool visited[MAX][MAX];

void bfs(int start, int end, char c){
    queue<pair<int, int>> q;
    visited[start][end] = true;
    q.push(make_pair(start, end));

    while(!q.empty()){
        int curX = q.front().first;
        int curY = q.front().second;
        q.pop();

        for(int i = 0; i < 4; i++){
            int x = curX + dx[i];
            int y = curY + dy[i];

            if((x >= 1 && x <= n) && (y >= 1 && y <= n) && !visited[x][y] && map[x][y] == c){
                visited[x][y] = true;
                q.push(make_pair(x, y));
            }
        }

    }
}

int main(){
    int cnt = 0;
    cin >> n;
    for(int i = 1; i <= n; i++)
        for(int j = 1; j <= n; j++)
            cin >> map[i][j];

    for(int i = 1; i <= n; i++)
        for(int j = 1; j <= n; j++)
            if (!visited[i][j]) {
                bfs(i, j, map[i][j]);
                cnt++;
            }
    cout << cnt << " ";
    
    for(int i = 1; i <= n; i++)
        for(int j = 1; j <= n; j++)
            visited[i][j] = false;
    
    cnt = 0;
    for(int i = 1; i <= n; i++)
        for(int j = 1; j <= n; j++)
            if (map[i][j] == 'G') map[i][j] = 'R';
    
    for(int i = 1; i <= n; i++)
        for(int j = 1; j <= n; j++)
            if (!visited[i][j]) {
                bfs(i, j, map[i][j]);
                cnt++;
            }
    cout << cnt;
    return 0;
}
