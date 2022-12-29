//
// Created by 전재현 on 2022/12/29.
//
#include <iostream>
#include <vector>
#include <cmath>
using namespace std;
#define MAX 10001
int main(){
    int n,k ;
    cin >> n >> k ;
    vector <int> v;
    for (int i = 1; i < n + 1; i++){
        if ( n % i == 0) v.push_back(i);
    }
    if (v.size() < k) cout << 0;
    else cout << v[k - 1];

}