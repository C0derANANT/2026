#include<stdio.h>
int main(){
    float basic_salary,da,hra,gross_salary;
    printf("Enter Basic Salary : ");
    scanf("%f",&basic_salary);
    da=basic_salary*0.4;
    hra=basic_salary*0.2;
    gross_salary=basic_salary+da+hra;
    printf("Gross Salary : %f\n",gross_salary);
    printf("DA : %f\n",da);
    printf("HRA : %f\n",hra);
}