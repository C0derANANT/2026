#include<stdio.h>
int main(){
    int days,years,months,rem_days,rem_months;
    printf("Enter Number Of Days : ");
    scanf("%d",&days);
    years=days/360;
    months=days/30;
    rem_months=months-years*12;
    rem_days=days-months*30;
    if(years>0){
        printf("%d Years ",years);
    }
    if(rem_months>0){
        printf("%d month ",rem_months);
    }
    if(rem_days>0){
        printf("%d days ",rem_days);
    }

}