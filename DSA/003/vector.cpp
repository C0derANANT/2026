#include<stdio.h>
#include<vector>
using namespace std;
int main(){
    vector<int> vec={10,9,8,7,6,5,4,3,2,1,0};
    printf("  Elements : Index\n");
    for(int i: vec){
        printf("\t%d : %d\n",i,vec[i]);
    }
    printf("Size of vector : %d\n",vec.size());
}
