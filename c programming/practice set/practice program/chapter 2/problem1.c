/*Write a program to check whether a number is divisible by 97 or 
not.  
*/
#include <stdio.h>

int main(){
    int a;
    printf("Enter the number :");
    scanf("%d", &a);
    if(a%97==0){
        printf("%d is dvisible by 97", a);
    }else{
        printf("%d is not divisible by 97",a);
    }
    return 0;
}