#include <stdio.h>

int main() {
    int a = 10;
    char name[] = "Anant Aggarwal";
    float decimal=5.6;
    printf("Integer: %d\n", a);
    printf("String: %s\n", name);
    printf("Float: %.2f\n", decimal);
    printf("Integer: %d\nFloat: %.2f\n",a,decimal);
    return 0;
}