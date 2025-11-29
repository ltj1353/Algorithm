#include <iostream>
#include <deque>
using namespace std;

int n;
long long a;
long long c[3000000];

int main() {
    
    cin >> a >> n;
    for (int i = 0; i < n; i++) cin >> c[i];

    deque<int> maxDeque; // 감소 덱, 윈도우 최대값
    deque<int> minDeque; // 증가 덱, 윈도우 최소값

    int fir = 0;
    long long ans = 0;

    for (int las = 0; las < n; las++) {
        // 최대값 덱 갱신
        while (!maxDeque.empty() && c[maxDeque.back()] <= c[las])
            maxDeque.pop_back();
        maxDeque.push_back(las);

        // 최소값 덱 갱신
        while (!minDeque.empty() && c[minDeque.back()] >= c[las])
            minDeque.pop_back();
        minDeque.push_back(las);

        // 슬라이딩 윈도우 조건 체크: max - min > a
        while (!maxDeque.empty() && !minDeque.empty() && c[maxDeque.front()] - c[minDeque.front()] > a) {
            // 왼쪽 포인터 이동
            if (maxDeque.front() == fir) maxDeque.pop_front();
            if (minDeque.front() == fir) minDeque.pop_front();
            fir++;
        }

        // 현재 윈도우 길이 갱신
        ans = max(ans, (long long)(las - fir + 1));
    }

    cout << ans;
    return 0;
}
