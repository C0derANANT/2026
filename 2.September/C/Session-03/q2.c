// UpperCase Or LowerCase
#include <stdio.h>
int main(){
    char ch;
    printf("Enter The Character : ");
    scanf("%c",&ch);
    if (ch>='A' && ch<='Z'){
        printf("UpperCase\n");
    }else if(ch>='a' && ch<='z'){
        printf("LowerCase\n");
    }else{
        printf("Not An Alphabet\n");
    }
    return 0;
}