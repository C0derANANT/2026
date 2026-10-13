// Bubble Sort


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
        printf("%d\n",arr[i]);
    }
    
    // Smallest Number In An Array
    // Sorting List
    for(int pass=0;pass<arr_size-1;pass++){
        for(int i=0;i<arr_size-1-pass;i++){
            if(arr[i]>arr[i+1]){
                int temp;
                temp=arr[i];
                arr[i]=arr[i+1];
                arr[i+1]=temp;
            }
        }
    }
    printf("[");
    for(int i=0;i<arr_size;i++){
        printf("%d",arr[i]);
        if(i<arr_size-1){
            printf(",");
        }
    }
    printf("]\n");
    printf("Smallest Number: %d\n",arr[0]);
    printf("Largest Number: %d\n",arr[arr_size-1]);
}