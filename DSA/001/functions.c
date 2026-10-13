// LeetCode 70
#include<stdio.h>
int factorial(int n ){
    int factorial=1;
    for(int i=1;i<=n;i++){
        factorial*=i;
    }
    return factorial;

    
}
int main(){
    int n=4,temp=n; // No Of Ways
    int max_2s=n/2;
    int count=0;
    for(int i=0;i<=max_2s;i+=1){
        temp=n-2*i;
        int ncr=factorial(temp+i)/(factorial(i)*factorial(temp));
        count+=ncr;
    }
    printf("%d\n",count);
}