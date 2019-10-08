#include <iostream>
using namespace std;
int main(){
    int k = 0;
    int p = 1;
    while(k<10001){
        p++;
        int is_prime = 1;
        for(int j=2; j<p; j++)
            if(p%j==0){
                is_prime = 0;
                break;
            }
        if(is_prime==1){
            k++;
            if(k%100==0){
                cout << k << endl;
            }
        }
    }
    cout << p << endl;
}