#include<stdio.h>
#include<vector>
using namespace std;
int main(){
    vector<int>arr={4,1,1,2,4,2,7,8,8};
    int single=0;
    for(int i:arr){
        single^=i;
    }
    printf("%d",single);
}

// /dragshutterflash