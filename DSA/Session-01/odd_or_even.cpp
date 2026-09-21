#include<stdio.h>
int main() {
    int a;
    printf("Enter A Number: ");
    scanf("%d",&a);
    if(a%2==0){
        printf("%d: Is An Even Number\n",a);
    }else{
        printf("%d: Is An Odd Number\n",a);
    }
    return 0;
}