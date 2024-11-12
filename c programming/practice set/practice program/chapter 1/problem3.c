// Write a program to convert Celsius (Centigrade degrees 
//temperature to Fahrenheit).
#include <stdio.h>

int main(){
    float c, f;
    printf("Enter the temperature in celcuius:");
    scanf("%f",&c);
    f= (c*(9.0/5.0))+32.0;
    printf("The temperature in farenhite is %.2f", f);
    return 0;
}