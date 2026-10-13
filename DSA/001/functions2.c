#include<stdio.h>
int prime(int n){
    printf("\nThe Function Invoked is: Prime Number Check\n");
    if(n <= 1){
        printf("%d is not a prime number\n", n);
        return 0;
    }
    for(int i = 2; i * i <= n; i++){
        if(n % i == 0){
            printf("%d is not a prime number\n", n);
            return 0;
        }else{
            printf("%d is a prime number\n", n);
            return 1;
        }
}}
// int prime_upto_n(int n){
//     printf("\nThe Function Invoked is: Prime Numbers up to n\n");
//     if (prime(n) == 1){
//         printf("%d is a prime number\n", n);
//     }
// }

// }

// int main(){
//     printf("\n----- Main Function -----\n");
//     int n;
//     printf("Enter A Number : ");
//     scanf("%d",&n);
//     prime(n);
// }