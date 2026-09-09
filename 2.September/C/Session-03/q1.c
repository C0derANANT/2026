// Grading System: 100
#include <stdio.h>
int main(){
    int marks;
    printf("Enter The Marks : ");
    scanf("%d",&marks);
    if (marks>=0 && marks <=100){
        if (marks>=90){
            printf("Grade : A+\n");
        }else if(marks>=70){
            printf("Grade : A\n");
        }else if(marks>=30){
            printf("Grade : B\n");
        }else{
            printf("Fail\n");
        }
    }else{
        printf("Invalid Marks Entered\n");
    }

}