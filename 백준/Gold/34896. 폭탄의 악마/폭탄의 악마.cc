//확인용입니다
#include <iostream>
#include <deque>
#include <algorithm>
using namespace std;

int a, d;
deque<int> b;
deque<int> c;
deque<deque<int>> list;
int ans = 0;
int tmp = 0;

bool check(const deque<deque<int>>& list, int rang) {
    int count = 0;
    int tmp_local = 10001;
    int e = list[0][0];

    for (int i = 0; i < (int)list.size(); i++) {
        if (e + rang < list[i][0]) {
            count += tmp_local;
            tmp_local = list[i][1];
            e = list[i][0];
        }
        else {
            tmp_local = min(tmp_local, list[i][1]);
            e = list[i][0];
        }
    }
    count += tmp_local;
    return count <= d;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> a;

    b.resize(a);
    for (int i = 0; i < a; i++) cin >> b[i];

    c.resize(a);
    for (int i = 0; i < a; i++) cin >> c[i];

    cin >> d;

    for (int i = 0; i < a; i++) {
        deque<int> row = { b[i], c[i] };
        list.push_back(row);
    }

    sort(list.begin(), list.end(), [](const deque<int>& x, const deque<int>& y) {
        return x[0] < y[0];
        });

    int left = 0;
    int right = list.back()[0] - list.front()[0];
    ans = right;

    while (left <= right) {
        int mid = (left + right) / 2;
        if (check(list, mid)) {
            ans = mid;
            right = mid - 1;
        }
        else {
            left = mid + 1;
        }
    }

    if (ans != 0)
        cout << ans;
    else
        cout << 1;
    return 0;
}
