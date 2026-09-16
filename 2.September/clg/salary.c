#include<stdio.h>
int main(){
    int basic_salary,da,hra,gross_salary;
    printf("Enter Basic Salary : ");
    scanf("%d",&basic_salary);
    da=basic_salary*0.4;
    hra=basic_salary*0.2;
    gross_salary=basic_salary+da+hra;
    printf("Gross Salary : %d\n",gross_salary);
    printf("DA : %d\n",da);
    printf("HRA : %d\n",hra);
}