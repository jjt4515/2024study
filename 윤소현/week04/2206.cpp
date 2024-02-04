#include <iostream>
#include <queue>
#include <string>
#define MAX 1001

using namespace std;

int n, m;
int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};
int map[MAX][MAX][2];
/*
map[][][0] -> 입력 값 및 벽 부수기 전 최단 거리
map[][][1] -> 벽을 부순 후 최단 거리
*/

queue<pair<int, pair<int, int> > > q;

void bfs(){
    q.push(make_pair(0, make_pair(0, 0)));
    /* q에 들어갈 내용은 벽을 부쉈는지?와 (x,y)좌표
        일단 (0,0)부터 들어가보자
    */
    while(!q.empty()){
        int broken = q.front().first;
        int curX = q.front().second.first;
        int curY = q.front().second.second;
        q.pop();        // 방문한 것은 q에서 빼자

        for(int i = 0; i < 4; i++){
            int x = curX + dx[i];
            int y = curY + dy[i];
            if (x < 0 || x >= n || y < 0 || y >= m)
                continue;

            if(map[x][y][0] == 1){      // 들어갈 수 없는 길이라면?
                if(!broken){            // 벽을 부순 적이 없다면?
                    map[x][y][broken + 1] = map[curX][curY][broken] + 1; 
                    // map[][][1] -> 벽을 부순 후 최단 거리이므로 broken+1에 현재 값에 대한 가중치?에 +1을 한다.
                    q.push(make_pair(1, make_pair(x, y)));  // 큐에 집어 넣고 탐색을 진행하자
                }
            }

            else if(map[x][y][0] == 0){     // 들어갈 수 있는 길이라면?
                if (broken == 1 && map[x][y][broken])   // 벽을 부순적이 있고 그 부분이 1 이상이라면 이미 탐색한 경우일 수밖에 없다. 
                  // 왜? 갈 수 있는 길은 애초에 다 0이기 때문에 즉 방문을 했으면 굳이 들어갈 필요가 없다.
                    continue;
                map[x][y][broken] = map[curX][curY][broken] + 1;
                q.push(make_pair(broken, make_pair(x, y)));
            }
        }

        if(curX == n-1 && curY == m-1){ 
            cout << map[n-1][m-1][broken]+1 << endl; // 목적지에 도달한 경우
            return;
        }
    }
    cout << -1 << endl;
    return;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n >> m;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++){
            char tmp;
            cin >> tmp;
            map[i][j][0] = tmp - '0';
        }
    bfs();
    return 0;
}
