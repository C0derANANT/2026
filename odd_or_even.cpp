#include<stdio.h>
int main() {
    int a;
    printf("Enter a number: ");
    scanf("%d", &a);
    if(a%2==0){
        printf("%d: Is Even\n",a);
    }else{
        printf("%d: Is Odd\n",a);
    }
    return 0;
}
