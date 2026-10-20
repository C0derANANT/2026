#include<stdio.h>
int main(){
    int n,divisor,count=0;
    printf("Enter A Number: ");
    scanf("%d",&n);
    printf("Enter A Divisor: ");
    scanf("%d",&divisor);
    while(1){
        if(n-divisor>0){
            count+=1;
            n=n-divisor;
            continue;
        }else{
            break;
        }
    }
    printf("%d\n",count);
    return 0;
}