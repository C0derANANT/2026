#include <stdio.h>

int main() {
    int n, reversed = 0;
    printf("Enter a number: ");
    scanf("%d", &n);
    
    int original = n;  // Keep for verification if needed
    
    while(n != 0) {
        reversed = reversed * 10 + (n % 10);  // Simpler approach
        n = n / 10;
    }
    
    printf("Reversed Number: %d\n", reversed);
    return 0;
}