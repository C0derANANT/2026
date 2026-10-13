// Linear Search

#include<stdio.h>
int main (){
    int arr[]={4,2,7,8,1,2,5};
    int target=8463;
    int index=-1;
    for (int i=0;i<sizeof(arr)/sizeof(arr[0]);i++){
        if(arr[i]==target){
            index=i;
            break;
        }
    }
    if(index==-1){
        printf("Index Not Found: -1\n");
    }
    else{
        printf("Index : %d\n",index);
    }
}