#include <stdio.h>

int main() {
    int number;

    printf("Enter The Number : ");
    scanf("%d", &number);

    for (int j = 1; j <= number; j++) {
        printf("\nTable of %d:\n", j);

        for (int i = 1; i <= 10; i++) {
            printf("%d x %d = %d\n", j, i, j * i);
        }
    }

    return 0;
}