#include<iostream>
#include<sstream>
#include<vector>

using namespace std;

int main() {
    string input, temp;
    getline(cin, input);
    stringstream ss(input);
    vector<int> a;
    int count = 1;
    
    while(getline(ss, temp, ',')) {
        a.push_back(stoi(temp));
        count++;
    }

    int sum = 0;
    int expected_sum = (int)(count * (count+1))/2;
    for (int num:a) {
        sum+=num;
    }

    cout << expected_sum - sum;

    return 0;
}
