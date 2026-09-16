#include<stdio.h>
int main(){
    int length,breadth;
    printf("Enter Length Of Rectangle: ");
    scanf("%d",&length);
    scanf("%d",&breadth);
    printf("Enter Breadth Of Rectangle: ");
    printf("Area : %d\n",length*breadth);
    printf("Perimeter : %d\n",2*(length+breadth));

}