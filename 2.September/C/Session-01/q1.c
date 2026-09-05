#include<stdio.h>
int main(){
    int side;
    printf("Enter Length Of A Side: ");
    scanf("%d",&side);
    printf("Area: %d\n",side*side);
    printf("Perimeter: %d\n",side*4);
    return 0;
}