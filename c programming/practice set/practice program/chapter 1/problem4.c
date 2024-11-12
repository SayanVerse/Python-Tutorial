/* Write a program to calculate simple interest for a set of values 
representing principal, number of years and rate of interest.*/

#include <stdio.h>

int main(){
    int t;
    float p,r;
    printf("Enter the principle amount:");
    scanf("%f", &p);
    printf("Enter interest rate:");
    scanf("%f", &r);
    printf("Enter the time periods:");
    scanf("%d", &t);
    printf("The interest is :%.2f %", p*r*t);
    return 0;
}