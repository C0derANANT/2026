// Pythagorean
#include<stdio.h>
int main(){
    int a ,b,c;
    printf("Enter First Number: ");
    scanf("%d",&a);
    printf("Enter Second Number: ");
    scanf("%d",&b);
    printf("Enter Third Number: ");
    scanf("%d",&c);
    if(a*a + b*b == c*c ){
        printf("Pythagorean Triplet\n");
        printf("%d^2 + %d^2 = %d^2\n",a,b,c);
    }else if(b*b + c*c == a*a){
        printf("Pythagorean Triplet\n");
        printf("%d^2 + %d^2 = %d^2\n",b,c,a);
    }else if(a*a + c*c == b*b){
        printf("Pythagorean Triplet\n");
        printf("%d^2 + %d^2 = %d^2\n",a,c,b);
    }
        else{
        printf("NOT A Pythagorean Triplet\n");
    }
}