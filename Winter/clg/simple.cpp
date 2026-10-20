#include <stdio.h>
int main() {
    int n;
    printf("Enter Number Of Rows: ");
    scanf("%d",&n);
    for(int i=1;i<=n;i++){
        for(int j=1;j<=i;j++){
            printf("* ");
        }
        for (int k=n-1;k<=1;k--){
            printf("* ");
            
        }
        printf("\n");
    }

    return 0;
}
