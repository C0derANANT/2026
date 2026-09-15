#include<stdio.h>
int main(){
    int n;
    printf("Enter A Number : ");
    scanf("%d",&n);
    for (int j=1;j<=n;j++){
        for(int i=1;i<=10;i++){
            printf("%d x %d = %d\n",j,i,j*i);
        }

    }
}