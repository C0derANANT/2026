#include <stdio.h>
int main() {
    int n;
    printf("Enter A Number: ");
    scanf("%d", &n);

    for (int row = 1; row <= 2 * n - 1; row++) {
        int stars;

        if (row <= n) {
            stars = n - row + 1;   
        } else {
            stars = row - n + 1;   
        }

        for (int s = 1; s <= n - stars + 1; s++) {
            printf(" ");
        }
        for (int j = 1; j <= stars; j++) {
            printf("* ");
        }
        printf("\n");
    }

    return 0;
}


// n=4
//  * * * * 
//   * * *
//    * *
//     *
//    * *
//   * * *
//  * * * * 
