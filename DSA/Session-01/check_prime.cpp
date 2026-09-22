#include<stdio.h>
int main(){
    int n;
    printf("Enter A Number: ");
    scanf("%d",&n);
    if(n <= 1){
        printf("%d: Not Prime\n", n);
        return 0;
    }
    for(int i=2; i*i<=n; i++){
        if(n%i==0){
            printf("%d: Not Prime\n", n);
            return 0;
        }
    }
    printf("%d: Prime\n", n);
    printf("Thank You For Using This Program\n");
    return 0;
}