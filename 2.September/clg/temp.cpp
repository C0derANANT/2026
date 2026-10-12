#include<stdio.h>
int main(){
    int a[4]={2,7,11,15};
    int target=9;
    for(int i=0;i<4;i++){
        for(int j=0;j<4;j++){
            if(a[i]<a[j]){
                if(a[i]+a[j]==target){
                    printf("[%d,%d]\n",a[i],a[j]);
                }
            }
        }
    }
    return 0;
}