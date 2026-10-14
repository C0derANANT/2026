// 2244 LeetCode
#include<stdio.h>
int main(){
    int count=0,tasks=0;
    int arr[]={2,2,3,3,2,4,4,4,4,4};
    for(int i=0;i<sizeof(arr)/sizeof(arr[0]);i++){
        count=0;
        for(int j=i+1;j<sizeof(arr)/sizeof(arr[0]);j++){

            if(arr[i]==arr[j]){
                count++;
            }
        }if(count%3==1){
            tasks+=(count-1)/3+2;
        }else if(count%3==2){
            tasks+=(count)/3+1;
        }else if(count==1){
            return -1;
    }
    printf("%d",tasks);
}}