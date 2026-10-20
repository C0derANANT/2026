// ODD or EVEN Number Using C Language
#include <stdio.h>
int main() {
    int num;
    printf("Enter A Number : ");

    scanf("%d",&num);
    if(num%2==0) {
        printf("%d Is An Even Number\n", num);
    } else {
        printf("%d Is An Odd Number\n", num);
    }
    return 0;
} 