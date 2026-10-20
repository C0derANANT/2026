#include <stdio.h>
int main() {
    int num;
    int digits = 0;
    printf("Enter A Number : ");
    scanf("%d", &num);
    if (num == 0) {
        digits = 1; 
    } else {
        for (; num != 0; num = num / 10) {
            digits++;
        }
    }
    printf("Number of digits: %d\n", digits);
    return 0;
} 

int addition(){
    int a , b;
    printf("Enter two numbers : ");
    
}