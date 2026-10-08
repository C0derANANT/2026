#include<stdio.h>
int main(){
    int n,matches;
    printf("Enter Number Of Teams: ");
    scanf("%d",&n);
    matches=0;
    while(n>1){
        if(n%2==0){
            matches+=n/2;
            n=n/2;
        }else{
            matches+=((n - 1) / 2);
            n=((n - 1) / 2+1);
        }
        
    }
    printf("Total Number Of Matches: %d\n",matches);
}