#include<stdio.h>
#include<vector>
using namespace std;
int main(){
    vector<int>vec={34,45,56,67,78,89,90};
    int tar=67;
    for(int i=0;i<vec.size();i++)
        if(tar==vec[i]){
            printf("Target Found At : %d\n",i);
        }
    else{
        printf("Target NOT Found At : -1\n");

    }
    }