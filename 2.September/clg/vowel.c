#include<stdio.h>
#include <string.h>

int main(){
    char ch;
    printf("Enter A Character : ");
    scanf("%c",&ch);
    if(tolower(ch)=='a'||tolower(ch)=='e'||tolower(ch)=='i'||tolower(ch)=='o'||tolower(ch)=='u'){
        printf("The Character Is A Vowel\n");
    }
    else{
        printf("The Character Is Not A Vowel\n");
    }
    return 0;
}\
