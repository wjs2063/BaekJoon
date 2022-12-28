//
// Created by 전재현 on 2022/12/29.
//
#include <iostream>
using namespace std;

int factorial(int n){
    if (n == 0) return 1;
    return n* factorial(n - 1);
}


int main(){
    long long n ;
    cin >> n;
    cout << factorial(n);

}