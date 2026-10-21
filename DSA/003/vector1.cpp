#include<stdio.h>
#include<vector>
#include<math.h>
#include<string.h>
using namespace std;

// int main(){
//     vector <int> vec= {34,54,76,78,89};
//     for(int i : vec){
//         printf("%d\n\n",i);
//     }
// }

// Decimal TO Binary Conversion
int main(){
    int n;
    vector<int>binary;
    printf("Enter A Decimal Number:  ");
    scanf("%d",&n);
    while(n>0){
        if(n%2==1){
            // printf("1");
            binary.push_back(1);
            n=n/2;
            
        }else{
            // printf("0");
            binary.push_back(0);
            n=n/2;
        }
    }

    for(int i : binary){
        printf("%d",binary.back());
        binary.pop_back();

    }printf("\n\n");
}