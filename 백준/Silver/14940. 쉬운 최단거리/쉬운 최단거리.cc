//
// Created by 전재현 on 2022/12/29.
//
#include <iostream>
using namespace std;
#include <vector>
#include <queue>
#include <sstream>
#define MAX 1001

vector <string> split(string input,string delimiter);
vector < vector <string>> graph;
vector <string> words;

typedef struct{
    int x;
    int y;

}pos;

int n,m;
int dp[MAX][MAX] ;

vector <string> split(string input, string delimiter){
    vector <string> result;
    long long pos = 0;
    string token = "";
    while ((pos = input.find(delimiter)) != string::npos){
        token = input.substr(0,pos);
        result.push_back(token);
        input.erase(0,pos + delimiter.length());
    }
    result.push_back(input);
    return result;
}



void bfs(pos p){
    int x,y,nx,ny;
    x = p.x;
    y = p.y;
    int dx[4] = {-1,1,0,0};
    int dy[4] = {0,0,-1,1};
    // 시작지점은 무조건 방문 이므로 0
    dp[p.x][p.y] = 0;
    queue <pos> q;
    q.push(p);
    while (!q.empty()){
        x = q.front().x;
        y = q.front().y;
        q.pop();
        for (int i = 0; i < 4 ; i++){
            nx = x + dx[i];
            ny = y + dy[i];
            // 방문할수없는 지점이면 패스
            if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
            // 먼저 방문 한 곳이거나 갈수없는곳이면 패스
            if (dp[nx][ny] != -1 || graph[nx][ny] == "0") continue;
            dp[nx][ny] = dp[x][y] + 1;
            q.push({nx,ny});
        }
    }
}

int main(){
    fill(&dp[0][0],&dp[MAX - 1][MAX - 1],-1);
    string input ;
    pos p;
    cin >> n >> m ;
    int sx,sy;
    cin.ignore();
    for (int i = 0 ; i < n ; i++){
        getline(cin,input);
        words = split(input," ");
        graph.push_back(words);
    }

    for (int i = 0 ; i < graph.size(); i++){
        for (int j = 0; j < graph[i].size();j++){
            if (graph[i][j] == "2"){
                p.x = i;
                p.y = j;
            }
            if (graph[i][j] == "0") dp[i][j] = 0;
        }
    }
    bfs(p);
    for (int i = 0;i < n ; i++){
        for (int j = 0 ; j < m ; j ++) {
            if (j == m - 1) {
                cout << dp[i][j] <<"\n" ;
                continue;
            }
            // 못가는 땅이면 0 출력하고

            if (graph[i][j] == "0") cout << 0 << " ";
            // 갈수있는 땅이면 그대로 출력
            else cout << dp[i][j] << " ";
        }
    }
}
