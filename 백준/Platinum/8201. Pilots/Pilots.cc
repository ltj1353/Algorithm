#include <iostream>
#include <deque>
using namespace std;

long long a;
int b;
long long c[3000000];

int main() {
    
    cin >> a >> b;
    for (int i = 0; i < b; i++)
        cin >> c[i];

    deque<int> maxi;
    deque<int> mini;

    int fir = 0;
    long long ans = 0;

    for (int las = 0; las < b; las++) {
        while (!maxi.empty() && c[maxi.back()] <= c[las])
            maxi.pop_back();
        maxi.push_back(las);

        while (!mini.empty() && c[mini.back()] >= c[las])
            mini.pop_back();
        mini.push_back(las);

        //cout << maxi[0] << mini[0] << endl;

        while (c[maxi[0]] - c[mini[0]] > a) {
            if (maxi[0] == fir)
                maxi.pop_front();
            if (mini[0] == fir)
                mini.pop_front();
            //cout << fir << las << endl;
            fir++;
        }
        ans = max(ans, (long long)(las - fir + 1));
    }

    cout << ans;
    return 0;
}
