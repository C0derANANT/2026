// #include <stdio.h>
// int main() {
//     int number;
//     printf("Enter an integer: ");
//     scanf("%d", &number);
//     if (number>0){
//         printf("The number is positive.\n");
//         if (number%2==0){
//             printf("The number is even.\n");
//         } else {
//             printf("The number is odd.\n");
//         }
//     } else if (number<0){
//         printf("The number is negative.\n");
//     } else {
//         printf("The number is zero.\n");
//     }
//     return 0; 
// }


// Marks Check
#include <stdio.h>
int main(){
    int marks;
    printf("Enter Marks : ");
    scanf("%d",&marks);
    if (marks>30){
        printf("PASS\n");
    }
    else{
        printf("FAIL\n");
    }
    printf("The Address of marks is : %p",&marks);
    return 0;
}
