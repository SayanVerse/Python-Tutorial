// Write a C program to calculate area of a rectangle:

#include<stdio.h>
int main()
{
    float length, width, area;
    printf("Enter the length:");
    scanf("%f", &length);
    printf("Enter the width:");
    scanf("%f", &width);
    area=length *width;
    printf("The area of the rectangle is : %.2f", area);
    return 0;
    
}