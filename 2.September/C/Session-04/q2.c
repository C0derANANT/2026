#include <stdio.h>
#include <string.h>
int main(){
    char name[] = "Hello World";
    for (int i=0;i<strlen(name);i+=1){
        printf("%c\n",name[i]);
    }
    return 0;
}