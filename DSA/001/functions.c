#include <stdio.h>

// Sum Of Two Numbers
int sum_of_two(){
    printf("\nThe Function Invoked is: Sum of Two Numbers\n");
    int a, b, sum;
    printf("Enter First Number: ");
    scanf("%d", &a);
    printf("Enter Second Number: ");
    scanf("%d", &b);
    sum = a + b;

    return sum;
}

// Minimum Of Two Numbers
int min_of_two(){
    printf("\nThe Function Invoked is: Minimum of Two Numbers\n");
    int min;
    int a, b;
    printf("Enter First Number: ");
    scanf("%d", &a);
    printf("Enter Second Number: ");
    scanf("%d", &b);
    if(a >= b){
        min = b;
    }
    else{
        min = a;
    }
    return min;
}

// Factorial helper (takes n as a parameter, no input/output)
long long factorial(int n){
    long long result = 1;
    for(int i = 1; i <= n; i++){
        result *= i;
    }
    return result;
}

// Factorial Of A Number (reads input, then uses the helper)
long long factorial_of_a_number(){
    printf("\nThe Function Invoked is: Factorial of A Number\n");
    int n;
    printf("Enter A Number: ");
    scanf("%d", &n);
    if(n < 0){
        printf("Factorial is not defined for negative numbers\n");
        return -1;
    }
    if(n > 20){
        printf("Number too large: factorial overflows beyond 20\n");
        return -1;
    }
    return factorial(n);
}

// Sum Of Digits
int sum_of_digits(){
    int n, sum = 0;
    printf("\nThe Function Invoked is: Sum of Digits\n");
    printf("Enter A Number: ");
    scanf("%d", &n);
    if(n < 0){
        n = -n;
    }
    while(n != 0){
        sum += n % 10;
        n /= 10;
    }
    return sum;
}

// Binomial Coefficient = nCr = n! / ((n-r)! * r!)
long long binomial(){
    int n, r;
    printf("\nThe Function Invoked is: Binomial Coefficient\n");
    printf("Enter n: ");
    scanf("%d", &n);
    printf("Enter r: ");
    scanf("%d", &r);
    if(n < 0 || r < 0 || r > n){
        printf("Invalid Input: need 0 <= r <= n\n");
        return -1;
    }
    if(n > 20){
        printf("n too large: factorial overflows beyond 20\n");
        return -1;
    }
    long long numerator = factorial(n);
    long long denominator = factorial(r) * factorial(n - r);
    return numerator / denominator;
}

// Main Function
int main(){
    printf("\n----- Main Function -----\n");
    // 1. Function --> Sum of two numbers
    int sum = sum_of_two();
    // 2. Function --> Minimum of two numbers
    int min = min_of_two();
    // 3. Function --> Factorial of a number
    long long fact = factorial_of_a_number();
    // 4. Function --> Sum of digits
    int digit_sum = sum_of_digits();
    // 5. Function --> Binomial Coefficient
    long long binomial_coeff = binomial();

    printf("\n----- Results -----\n");
    printf("Sum of two numbers is: %d\n", sum);
    printf("Minimum of two numbers is: %d\n", min);
    if(fact >= 0){
        printf("Factorial of a number is: %lld\n", fact);
    }
    printf("Sum of digits is: %d\n", digit_sum);
    if(binomial_coeff >= 0){
        printf("Binomial Coefficient is: %lld\n", binomial_coeff);
    }
    return 0;
}