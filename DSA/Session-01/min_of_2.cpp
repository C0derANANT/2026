#include<stdio.h>
int main() {
    int a, b;
    printf("Enter First Number: ");
    scanf("%d",&a);
    printf("Enter Second Number: ");
    scanf("%d",&b);
    if(a<b){
        printf("%d: Is The Smallest\n",a);
    }else if(a>b){
        printf("%d: Is The Smallest\n",b);
    }else{
        printf("%d:Both Are Equal\n",a);
    }
    return 0;
}