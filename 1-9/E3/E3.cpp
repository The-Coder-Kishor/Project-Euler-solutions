#include<iostream>
using namespace std;

int main() {
    long long int num = 600851475143;
    int d  = 2;
    while(num > 1) {
        if(num%d==0) {
            num /= d;
        }
        else {
            d += 1;
        }
    }
    cout<<d<<endl;
}
