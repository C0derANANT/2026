// Perfect Number
#include <stdio.h>

int main() {
    int n, factors_sum = 0;
    printf("Enter A Number: ");
    scanf("%d", &n);

    for (int i = 1; i <= n / 2; i++) {
        if (n % i == 0) {
            factors_sum += i;
        }
    }

    if (factors_sum == n && n > 0) {
        printf("Perfect Number\n");
    } else {
        printf("NOT A Perfect Number\n");
    }
    return 0;
}