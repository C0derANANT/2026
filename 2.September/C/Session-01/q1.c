#include<stdio.h>
int main(){                     
    int side;
    printf("Enter Length Of A Side: ");
    scanf("%d",&side);
    printf("Area: %d sq.units\n",side*side);             // AREA OF A Square
    printf("Perimeter: %d units\n",side*4);           // Perimeter OF A Square
    return 0;
}

// --------------x--------------x--------------x--------------x--------------x------

// #include<stdio.h>
// int main(){                     
//     float radius;
//     printf("Enter Radius Of A Circle: ");
//     scanf("%f",&radius);
//     printf("Area: %f sq.units\n",3.14*radius*radius);     // AREA OF A Circle
//     printf("Circumference: %f units\n",2 *3.14*radius); // Circumference OF A Circle
//     return 0;
// }