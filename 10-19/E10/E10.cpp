#include <bits/stdc++.h>
using namespace std;

int prime(long long n) {
    int i;
    for (i = 2; i * i <= n; i++) {
        if (n % i == 0) {
            return 0;
        }
    }
    return 1;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    long long sum = 0LL;
    for (long long  i = 2LL; i <= 2000000LL; i++) {
        if (prime(i)) {
            sum = sum + i;
        }
    }
    cout << sum << endl;
    return 0;
}
