//
// Created by 전재현 on 2022/12/29.
//
#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <algorithm>
using namespace std;
#define MAX 26

typedef struct {
    int x;
    int y;
}pos;

int n ;
int visited[MAX][MAX] = {0,};
vector <string> graph;



int bfs(pos p){
    queue <pos> q;
    q.push(p);
    //현재 노드 방문체크
    visited[p.x][p.y] = 1;
    int dx[4] = {-1,1,0,0};
    int dy[4] = {0,0,-1,1};
    int x,y,nx,ny;
    int house = 1;
    while ( !q.empty()){
        x = q.front().x;
        y = q.front().y;
        q.pop();
        for (int i = 0 ; i < 4 ; i++){
            nx = x + dx[i];
            ny = y + dy[i];
            // 방문했던경우나 집이없거나 범위벗어나면 패스
            if ( nx < 0 || nx >= n || ny < 0 || ny >= n || visited[nx][ny] == 1 || graph[nx][ny] == '0')continue;
            // 방문체크
            visited[nx][ny] = 1;
            house += 1;
            q.push({nx,ny});
        }
    }
    return house;

}

int main(){
    cin >> n;
    for (int i = 0; i < n; i++){
        string x;
        cin >> x;
        graph.push_back(x);
    }
    int cnt = 0;
    vector <int> ans;
    for (int i = 0; i < n ; i++){
        for (int j = 0 ; j < n ; j++){
            // 방문하지않은곳이며 집이있는곳이면 bfs 수행
            if (visited[i][j] == 0 && graph[i][j] == '1'){
                cnt += 1;
                ans.push_back(bfs({i,j}));
            }
        }
    }
    sort(ans.begin(),ans.end());
    cout << cnt << endl;
    for (auto i = ans.begin(); i < ans.end();++i){
        cout << *i << endl;
    }


}