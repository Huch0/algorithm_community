#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0); cin.tie(0);
    int N; cin >> N;
    vector<int> v;
    generate_n(back_inserter(v), N, [] () {return *(istream_iterator<int>{cin});});
    sort(v.begin(), v.end());

    int start = 0, end = N-1, ans1, ans2;
    int cmp = 2e9 + 1;
    while (start < end) {
        int now = v[start] + v[end]; // now = abs(v[start] + v[end])로 했더니 밑에 {-4, -3, -2, -1} 이런 경우 밑에 if-elif-elif 에서 문제 발생
        if (abs(now) < cmp) {
            cmp = abs(now);
            ans1 = v[start];
            ans2 = v[end];
        }

        if (now > 0) end--;
        else if (now < 0) start++;
        else if (now == 0) break;
    }
    cout << ans1 << ' ' << ans2;
}