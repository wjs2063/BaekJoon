//
// Created by 전재현 on 2023/01/04.
//


#include <iostream>
#include <algorithm>
#define MAX 21
#define INF 0xFFFFFFFFF
using namespace std;

long long  dp[MAX][2] ;
int rock[MAX][2] = {{0,0},};


int main(){
    int n,a,b,k;
    cin >> n ;
    for (int i = 1; i < n; i++){
        cin >> a >> b ;
        rock[i][0] = a;
        rock[i][1] = b;
    }
    fill(&dp[0][0],&dp[MAX][1],INF);
    cin >> k;
    // 초기값 설정
    dp[1][0] = 0;
    dp[1][1] = 0;

    for (int i = 2; i < n + 1; i++){
        if (i - 1 >= 1){
            dp[i][0] = min(dp[i][0],dp[i - 1][0] + rock[i - 1][0]);
            dp[i][1] = min(dp[i][1],dp[i - 1][1] + rock[i - 1][0]);
        }
        if (i - 2 >= 1) {
            dp[i][0] = min(dp[i][0], dp[i - 2][0] + rock[i - 2][1]);
            dp[i][1] = min(dp[i][1], dp[i - 2][1] + rock[i - 2][1]);
        }
        if (i - 3 >= 1) {
            dp[i][0] = min(dp[i][0], dp[i - 3][1] + k);
        }
    }
    cout << min(dp[n][0],dp[n][1]);


}