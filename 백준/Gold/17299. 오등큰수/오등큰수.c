#include <stdio.h>


typedef struct custom{
    int val;
    int idx;
}custom;

int main() {
    int n ;
    int max = 1000000;
    scanf("%d",&n);
    int a[n] ;
    for (int i = 0;i < n ;i++){
        scanf("%d",&a[i]);
    }
    /*
     *     for(int i = 0;i < n ;i++){
        printf("%d",a[i]);
    }
     * */
    int counter_a[max + 1] ;
    for (int i = 0; i < max + 1; i++){
        counter_a[i] = 0;
    }
    for (int i = 0;i < n;i++){
        counter_a[a[i]] += 1;
    }
    custom stack[n];
    int ans[n];
    // 배열 초기화
    for (int i = 0;i < n ;i ++){
        ans[i] = -1;
    }
    int top = -1;
    int v = -1;
    for (int i = 0;i < n ;i ++){
        v = a[i];
        while (top >= 0 && (counter_a[stack[top].val] < counter_a[v])) {
            ans[stack[top].idx] = v;
            top -= 1;
            }
        top += 1;
        stack[top].val = v;
        stack[top].idx = i;
    }
    for (int i = 0;i < n ;i ++){
        if (i != n - 1){
            printf("%d ",ans[i]);
        }
        else{
            printf("%d",ans[i]);
        }
    }

    return 0;
}
