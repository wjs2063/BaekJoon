#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

bool solution(int x) {

    int a = 0;
    int n = x;
    if(x>0 && x<10){
        return true;
    }
    while (n > 0){
        a += n % 10;
        n /= 10;
    }
    if ( x % a == 0) return true;
    return false;

}