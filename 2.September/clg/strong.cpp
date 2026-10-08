// Strong Number
#include<stdio.h>
int main(){
    int n, sum = 0, temp, digit;
    printf("Enter a number: ");
    scanf("%d", &n);
    temp = n;
    while(temp > 0){
        digit = temp % 10;
        int fact = 1;
        for(int i = 1; i <= digit; i++){
            fact *= i;
        }
        sum += fact;
        temp /= 10;
    }
    if(sum == n){
        printf("%d is a Strong Number\n", n);
    }
    else{
        printf("%d is not a Strong Number\n", n);
    }
    return 0;
}