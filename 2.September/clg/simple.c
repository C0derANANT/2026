// Simple Interest Calculation Program in C
#include <stdio.h>
#include <stdbool.h>
int main(){
    float principal;
    printf("Enter The Principal Amount : ");
    scanf("%f", &principal);
    float rate;
    printf("Enter The Rate Of Interest : ");
    scanf("%f", &rate);
    float time;
    printf("Enter The Time (In Years) : ");
    scanf("%f", &time);
    float SI;
    SI=(principal*rate*time)/100;
    printf("Simple Interest : %.2f\n", SI);
    return 0;
}