#include <string>
#include <vector>
#include <algorithm>
#include <vector>
using namespace std;
#include <stdio.h>
#include <iostream>
int solution(vector<int> stones, int k) {
    int answer = 0;
    long long int sn,en,cnt,flag,ans,mid;
    sn = *min_element(stones.begin(),stones.end());
    en = *max_element(stones.begin(),stones.end());
    ans = 0;
    int n = stones.size();
    while (sn <= en){
        mid = sn + (en - sn) / 2;
        cnt = 0;
        flag = 0;
        for (int i = 0; i < n; i++){
            if (stones[i] - (mid - 1) <= 0 ){
                cnt += 1;
            }
            else{
                cnt = 0;
            }
            if (cnt >= k){
                flag = 1;
                break;
                
            }
            
        }
        if (flag){
            en = mid - 1;
        }
        else{
            ans = mid;
            sn = mid + 1;
        }
    }
    return ans;
}