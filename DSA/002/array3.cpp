// Two Pointer Approach
// Reversing An Array
#include<stdio.h>
int main(){
    int arr_size;
    printf("Enter Size Of The Array: ");
    scanf("%d",&arr_size);
    int arr[arr_size];
    printf("Enter Elements In The Array:\n");
    for(int i=0;i<arr_size;i++){
        printf("Enter %d Element: ",i+1);
        scanf("%d",&arr[i]);
    }
    for(int i=0;i<arr_size;i++){
        printf("%d ",arr[i]);
    }printf("\n");
    
    // Yaha tk ek array ka size aur elements input karne ka code hai
    // Ab
    // Reversing The Array
    
    for (int i=0;i<=arr_size/2;i+=1){
        int temp=arr[i];
        arr[i]=arr[arr_size-i-1];
        arr[arr_size-i-1]=temp;
    }
    
    for(int i=0;i<arr_size;i++){
        printf("%d ",arr[i]);
    }printf("\n");
}