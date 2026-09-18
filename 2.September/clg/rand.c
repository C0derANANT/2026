#include <stdio.h>
int main(){
    int body_count;
    printf("Enter the number of bodies: ");
    scanf("%d", &body_count);
    if(body_count==0){
        printf("Sanskari\n");
    }else if(body_count==1){
        printf("Managable\n");
    }else{
        printf("Randi\n");
    }
    return 0;
}
// Brazil Body Count 0