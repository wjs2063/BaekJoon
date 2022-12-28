//
// Created by 전재현 on 2022/12/29.
//
#include <iostream>
using namespace std;
#define MAX 91
int main(){
    int n;
    cin >> n;
    // data 크기를 넘는다 long long 은 8바이트 
    long long dp[MAX] = {0,};
    dp[0] = 0;
    dp[1] = 1;
    for (int i = 2 ; i < n + 1; i ++){
        dp[i] = dp[i - 1] + dp[i - 2];

    }
    cout << dp[n] << "\n";


}