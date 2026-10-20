// n=5
// 1 2 3 4 5
// 5 4 3 2 1
// 1 5 
#include<stdio.h>
int main()
{
    int n;
    printf("Enter A Number : ");
    scanf("%d",&n);
    for(int i=1;i<=n;i++){
        printf("%d ",i);
    }
    printf("\n");
    for(int i=n;i>=1;i--){
        printf("%d ",i);
    }
    printf("\n");
    printf("%d\n",(n*(n+1))/2);
}