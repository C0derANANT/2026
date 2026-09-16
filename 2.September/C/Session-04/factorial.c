#include <stdio.h>
int main()
{
    int n, factorial;
    printf("Enter A Number");
    scanf("%d", &n);
    factorial = 1;
    for (int i = 1; i <= n - 1; i += 1)
    {
        factorial *= i;
        printf("%d", i);
        if (i < n - 1)
            printf(" x ");
    }
    printf(" x %d = %d", n, factorial * n);
    return 0;
}