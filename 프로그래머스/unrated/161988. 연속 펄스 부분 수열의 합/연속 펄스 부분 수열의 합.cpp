#include <string>
#include <vector>
#include <math.h>

using namespace std;

long long solution(vector<int> sequence) {
    long long answer = 0;
    vector<long long> dp1, dp2;
    long long plus = 1;
    long long minus = -1;
    long long m = sequence[0];

    dp1.push_back(m);
    dp2.push_back(m * -1);
    if (m < dp1[0]) m = dp1[0];
    if (m < dp2[0]) m = dp2[0];
    
    for (int i = 1; i < sequence.size(); i++) {
        plus *= -1; minus *= -1;
        dp1.push_back(max(sequence[i] * plus, dp1[i - 1] + sequence[i] * plus));
        dp2.push_back(max(sequence[i] * minus, dp2[i - 1] + sequence[i] * minus));


        if (m < dp1[i]) m = dp1[i];
        if (m < dp2[i]) m = dp2[i];
    }

    return m;
}
