#include <bits/stdc++.h>

using namespace std;

// const string mess = "|_/=\\^'y |)@^n {_a`[\\/] g0^'[";

const int n = mess.size();

int k = 179;

int main()
{
    freopen("message.txt", "r", stdin);
    string mess;
    cin >> mess;
    cout << "k = " << k << '\n';
    cout << mess << "\n";
    cout << "len = " << mess.size() << '\n';
    vector<bool> a;
    for (char c : mess) {
        c ^= k;
        for (int i = 7; i >= 0; --i) {
            a.push_back((c & (1 << i)) >> i);
        }
    }
    assert(a.size() % 5 == 0);
    for (size_t i = 0; i < a.size(); i += 5) {
        char x = 0;
        for (int j = i; j < i + 5; ++j) {
            x = x * 2 + a[j];
        }
        x += 32;
        cout << x;
    }
    cout << "END";
    return 0;
}
