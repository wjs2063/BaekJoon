#include <string>
#include <vector>
#include <queue>
using namespace std;
#define MAX 101
int solution(vector<vector<int>> board) {
    int answer = 0;
    int x,y,nx,ny;
    queue <pair<int,int>> q;
    int n = board.size();
    int m = board[0].size();
    int visited[MAX][MAX] = {0,};
    for (int i = 0 ; i < n ; i++){
        for (int j = 0; j < m ; j++){
            if (board[i][j] == 1) q.push({i,j});
        }
    }
    int cnt = 0;
    while (!q.empty()){
        x = q.front().first;
        y = q.front().second;
        q.pop();
        for ( int dx = -1 ; dx < 2; dx++){
            for (int dy = -1; dy < 2; dy++){
                nx = x + dx;
                ny = y + dy;
                if (nx < 0 || nx > n - 1 || ny < 0 || ny > m - 1 )  continue;
                if (visited[nx][ny] == 0){ 
                    visited[nx][ny] = 1;
                    cnt += 1;
                }
            }
        }
        
        
    }
    
    return n*m - cnt;
}