# include <stdio.h>
int main(){
    int n;
    printf("Enter A Number : ");
    scanf("%d",&n);
    int sum=0;
    for(int i=1;i<=n;i++){
        sum+=i;
    }
    printf("Sum of first %d natural numbers is %d\n",n,sum);
    return 0;
}