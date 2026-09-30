// Strong Number Check
#include <stdio.h>

int main() {
    int n, originalNumber, digit;
    int sum = 0;

    printf("Enter a number: ");
    scanf("%d", &n);
    originalNumber = n;

    while (n > 0) {
        digit = n % 10;
        int factorial = 1;
        for (int i = 1; i <= digit; i++) {
            factorial *= i;
        }
        sum += factorial;
        n /= 10;
    }

    if (sum == originalNumber) {
        printf("Strong Number\n");
    } else {
        printf("Not A Strong Number\n");
    }
    return 0;
}