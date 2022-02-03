#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    //initializing ifstream class object
    ifstream fin;
    // creating an object with input.txt
    fin.open("input.txt");     

    string line;
    string num;

    //using stringstream to convert string to int
    stringstream ss;

    long long sum = 0LL;
    while(fin) {
        num = "";
        getline(fin, line);
        for (int i = 40; i <= 49; i++) {
            num += line[i];
        }
        ss << num;
        long long n;
        ss >> n;
        ss.clear();
        sum += n;
    }
    //closing it
    fin.close();

    //printing the sum to the file
    ofstream fout;
    fout.open("output.txt");
    fout << sum;
    fout.close();
    return 0;
}