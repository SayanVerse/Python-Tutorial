// write a program to convert farenhite to celcius

#include <stdio.h>

int main(){
    float farenhite, celcius;
    printf("Enter the farenhite temperature:");
    scanf("%f",&farenhite);
    
    celcius= (farenhite - 32.0) * (5.0/9.0);
    printf("the celcius temperature is : %.2f", celcius);

    return 0;
}