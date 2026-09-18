#include <stdio.h>
int main(){
    int body_count;
    printf("Enter the number of bodies: ");
    scanf("%d", &body_count);
    if(body_count==0){
        printf("Sanskari");
    }else if(body_count==1){
        printf("Managable");
    }else{
        printf("Randi");
    }
    return 0;
}