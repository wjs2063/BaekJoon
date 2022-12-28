#include <string>
#include <vector>

using namespace std;

vector<int> solution(int num, int total) {
    vector<int> answer;
    int t = num / 2;
    if (num % 2 == 1){
        int x = total / num ;
        for (int i = -t; i < t + 1; i++){
            answer.push_back(x + i);
        }
    }
    else{
        int x = (total - t ) / num;
        for ( int i = -t + 1; i < t + 1; i++ ){
            answer.push_back(x + i);
        }
    }
    return answer;
}