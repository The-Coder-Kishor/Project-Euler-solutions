#include <bits/stdc++.h>
using namespace std;

int numOfDivisors(int n) {
    int count = 0;
    for (int i = 1; i <= sqrt(n); i++) {
        if (i == sqrt(n)) {
            count += 1;
        }
        else if (n % i == 0) {
            count += 2;
        }
    }
    return count;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int i = 1, j = 0;
    while (true) {
        j = i * (i + 1) / 2;
        if (numOfDivisors(j) > 500) {
            cout << j << endl;
            break;
        }
        i++;
    } 
    return 0;
}