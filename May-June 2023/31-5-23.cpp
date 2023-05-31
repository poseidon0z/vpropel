#include <iostream>
using namespace std;

int main(){
    long long n,k;
    cin >> n >> k;
    long long out = k * (k-1);
    if ((n-out) % k == 0) {
        for (long long i = 0; i < k; i++){
            cout << (n-out) / k + i * 2 << "\t";
        }
    } else {
        cout << "Cannot be built";
    }
    
    return 0;
}
