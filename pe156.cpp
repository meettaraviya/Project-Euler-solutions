#include <stdio.h>
using namespace std;

int main(){
    unsigned long long upper = 10000000000ULL;

    unsigned long long count[10] = {0ULL, 0ULL, 0ULL, 0ULL, 0ULL, 0ULL, 0ULL, 0ULL, 0ULL, 0ULL};
    unsigned long long sum[10] = {0ULL, 0ULL, 0ULL, 0ULL, 0ULL, 0ULL, 0ULL, 0ULL, 0ULL, 0ULL};
    unsigned long long ans_count[10] = {0ULL, 0ULL, 0ULL, 0ULL, 0ULL, 0ULL, 0ULL, 0ULL, 0ULL, 0ULL};

    for(unsigned long long i=0; i<=upper; i++){
        unsigned long long i_copy = i;
        while(i_copy>0){
            count[i_copy%10]++;
            i_copy /= 10;
        }
        for(int j=1; j<10; j++){
            if(count[j]==i){
                sum[j]+=i;
                ans_count[j]++;
                printf("%d %llu %llu\n", j, i, sum[j]);
            }
        }
        if(i%10000000ULL == 0){
            printf("%llu\n", i);
        }
    }
    for(int i=1; i<10; i++){
        printf("%d %llu %llu\n", i, ans_count[i], sum[i]);
    }
}