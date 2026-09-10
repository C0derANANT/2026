// kmph to miles
#include <stdio.h>
int main(){
    float km;
    printf("Enter Distance in km:");
    scanf("%f",&km);
    float miles;
    miles=1.6*km;
    printf("Miles: %.2f\n",miles);
    return 0;
}