#include<stdio.h>
#include<math.h>
int main(){
    int n,digit,sum,temp,rem,i=0,fsum=0;
    printf("Enter Any Number: ");
    scanf("%d",&n);
    temp = n;
    int count,temp2;
    temp2 = n;
    while(1){
        if(temp2 == 0){
            break;
        }
        temp2 = temp2 / 10;
        i++;
    }

    while(1){
        if(temp==0){
            break;
        }
        rem = temp%10;
        sum = (pow(rem,i));
        fsum +=sum;
        temp = temp / 10;
        
    }
    if(fsum == n){
        printf("The input number %d = %d is amstrong number",fsum,n);
    }
    else{
        printf("the input number %d != %d is not amstrong number",fsum,n);
    }
    return 0;
}