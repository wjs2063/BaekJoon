//
// Created by 전재현 on 2022/12/29.
//
#include <iostream>
#include <vector>
using namespace std;
#define MAX 101

int main(){
    int dp[MAX] = {0};
    int n,m;
    vector <int> guest;
    cin >> n;
    for (int i = 0 ; i < n ; i++){
        cin >> m;
        guest.push_back(m);
    }
    int cnt = 0;
    for (auto i = guest.begin(); i != guest.end(); ++i){
        if (dp[*i] == 0) {
            dp[*i] = 1;
        }
        else cnt += 1;
    }
    cout << cnt;

}