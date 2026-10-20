#include<stdio.h>
int main(){
    int size;
    printf("Enter The Size Of The Array : ");
    scanf("%d",&size);
    int arr[size];
    for(int i=0;i<size;i++){
        printf("Enter Element Number %d: ",i+1);
        scanf("%d",&arr[i]);
    }
}