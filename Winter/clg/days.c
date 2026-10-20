#include <stdio.h>
#include <stdbool.h>

int main(){
    int months[12] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    
    int total_days, years = 0, months_count = 0, remaining_days;
    
    printf("Enter Number Of Days: ");
    scanf("%d", &total_days);
    
    if(total_days <= 0) {
        printf("Please enter a positive number of days!\n");
        return 1;
    }
    remaining_days = total_days;
    years = remaining_days / 365;
    remaining_days = remaining_days % 365;
    
    for(int i = 0; i < 12; i++) {
        if(remaining_days >= months[i]) {
            remaining_days -= months[i];
            months_count++;
        }
        else {
            break;  
        }
    }
    
    printf("\n===== RESULT =====\n");
    printf("Total Days: %d\n", total_days);
    printf("Years: %d\n", years);
    printf("Months: %d\n", months_count);
    printf("Remaining Days: %d\n", remaining_days);
    
    return 0;
}