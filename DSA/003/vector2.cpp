// Single Number in an array where every other number occurs twice
#include<iostream>
#include<vector>
using namespace std;
int main(){
    int arr[]={4,1,2,1,2,};
    int count=0;
    for(int i=0;i<sizeof(arr)/sizeof(arr[0]);i++){
        for(int j=i+1;j<sizeof(arr)/sizeof(arr[0]);j++){
            if(arr[i]==arr[j]){
                count+=1;
                if(count==1){
                    cout<<"Single Number : "<<arr[i]<<endl;
                }
            }
        }
        
    }
}