#include <stdio.h>
int main(){
    int num1,num2;
    printf("Enter The First Number : ");
    scanf("%d",&num1);
    printf("Enter The Second Number : ");
    scanf("%d",&num2);
    printf("Which Operation You Want To Perform : \n");
    printf("1. Addition\n");
    printf("2. Subtraction\n");
    printf("3. Multiplication\n");
    printf("4. Division\n");
    int choice;
    printf("Enter Your Choice : ");
    scanf("%d",&choice);
    switch(choice){
        case 1:
            printf("Addition : %d\n",num1+num2);
            break;
        case 2:
            printf("Subtraction : %d\n",num1-num2);
            break;
        case 3:
            printf("Multiplication : %d\n",num1*num2);
            break;
        case 4:
            if(num2!=0){
                printf("Division : %.2f\n",(float)num1/num2);   
            }
            else{
                printf("Division By Zero Is Not Possible\n");
            }
            break;
        default:
            printf("Invalid Choice\n");
        }
    return 0;
}   