#include<iostream>
using namespace std;

int main() {
    int a = 1;
    int b  = 2;
    int sum = 2;
    int c = a + b;
    while(c <= 4000000) {
        if(c%2==0) {
            sum += c;
        }
        a = b;
        b = c;
        c = a + b;
    }
    cout<<sum<<endl;
}
