#include <stdio.h>
// XOR between same bits = 0
// XOR between different bits = 1
// Variable Declaration
int main() {
    int OldAge = 20;
    int YearsPassed = 5;
    int NewAge = OldAge + YearsPassed;
    printf("New Age: %d\n", NewAge);

// Comparison Operators
    printf("2 == 3: %d\n", 2 == 3);
    printf("2 != 3: %d\n", 2 != 3);
    printf("2 < 3: %d\n", 2 < 3);
    printf("2 > 3: %d\n", 2 > 3);
// Logical Operators
    printf("2 && 3: %d\n", (2>3) && (3>2));
    printf("2 || 3: %d\n", (2>3) || (3>2));
    printf("!2: %d\n", !(2>3));
    return 0;
} 
