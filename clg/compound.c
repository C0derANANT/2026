// A=P(1+r/n)^(nt)

#include <stdio.h>
#include <math.h>
int main(){
    float principal;
    float rate;
    float time;
    float n;
    float A;
    printf("Enter The Principal Amount : ");
    scanf("%f", &principal);
    printf("Enter The Rate Of Interest : ");
    scanf("%f", &rate);
    printf("Enter The Time (In Years) : ");
    scanf("%f", &time);
    printf("Enter The Compounding Frequency : ");
    scanf("%f", &n);
    A=principal*pow(1+(rate/n), n*time);
    printf("Amount : %.2f\n", A);

}