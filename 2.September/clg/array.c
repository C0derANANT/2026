#include<stdio.h>
int main()
{
    // 
    int arr[5],sum=0,avg=0;
    printf("Enter 5 elements of the array:\n");
    for(int i = 0; i < 5; i++)
    {
        scanf("%d", &arr[i]);
    }
    // Printing Elements
    printf("\nPrint Elements Of The Array: \n");
    for (int i=0;i<5;i++){
        printf("%d\n",arr[i]);
    }
    // Sum Of Elements
    for (int i=0;i<5;i++){
        sum+=arr[i];
    }
    printf("Sum Of Elements Is : %d\n",sum);
    // Average Of Elements
    avg=sum/5;
    printf("Average Of Elements: %d\n",avg);

    // Largest Element In Array
    for(int i=0;i<5;i++){
        for(int j=i+1;j<5;j++){
            if(arr[i]<arr[j]){
                int temp=arr[i];
                arr[i]=arr[j];
                arr[j]=temp;
            }
        }
    }
    printf("Largest Element In Array: %d\n",arr[0]);
    printf("Smallest Element In Array: %d\n",arr[4]);
    return 0;
}