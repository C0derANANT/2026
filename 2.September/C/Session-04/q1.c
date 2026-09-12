#include <stdio.h>
#include <string.h>

int main(void) {
    char str[] = "Hello World!";

    for (size_t i = 0; i < strlen(str); i++) {
        printf("%c\n", str[i]);
        // or: putchar(str[i]);
    }
    return 0;
}