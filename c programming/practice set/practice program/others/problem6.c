// leap year using if else statement in c

#include <stdio.h>

int main(){
    int year;
    printf("Enter the year:");
    scanf("%d", &year);
    if((year % 4 ==0 && year % 100 != 0 ) || (year % 400 ==0)){
        printf("%d is a leapyear!", year);
    }
    else{
        printf("%d is not a leapyear!", year);
    }
    return 0;
}