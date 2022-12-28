//
// Created by 전재현 on 2022/12/29.
//
#include <iostream>
#include <string>
using namespace std;
#define MAX 300

int main(){
    string word;
    cin >> word;
    int count[MAX] = {0,};
    int max_val = 0;
    int index = 0;
    int cnt = 0;
    for ( int i = 0 ; i < word.size();i++){
        count[toupper(word[i])] += 1;
    }
    for (int i = 0 ; i < MAX ;i ++){
        // 최댓값 찾기
        if (count[i] > 0 && count[i] > max_val){
            max_val = count[i];
            index = i;
        }
    }
    for ( int i = 0; i < MAX ; i++){
        if (count[i] == max_val) cnt++;

    }
    if (cnt > 1) cout << "?";
    else{
        cout << (char)index;

    }

}