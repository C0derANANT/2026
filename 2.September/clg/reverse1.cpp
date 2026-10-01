#include<stdio.h>
int main(){
    int n,rev=0,original;
    printf("Enter A Number: ");
    scanf("%d",&n);
    original=n;
    if(n>0)
    while(n>0){
        rev=rev*10+n%10;
        n=n/10;
    }
    printf("%d\n",rev);
    if(original==rev){
        printf("Palindrome");
    }else{
        printf("NOT A Palindrome");
    }
}