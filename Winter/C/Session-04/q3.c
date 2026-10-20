#include <stdio.h>
int main(){
    int n;
    printf("Enter The Number : ");
    scanf("%d",&n);
    for (int i=1;i<=n;i++){
        if (n%i==0){
            printf("Even:%d\n",i);
        }else{
            printf("Odd:%d\n",i);
        }
    }
}