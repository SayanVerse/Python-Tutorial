//• Calculate the area of a circle and modify the same program to 
//alculate the volume of a cylinder given its radius and height.  

#include<stdio.h>
#define PI 3.14

int main()
{
    float r,h,a,v;
    printf("Enter the radius:");
    scanf("%f", &r);
    a=PI*r*r;
    printf("The area of the circle is : %.2f\n", a);
    printf("Now finding the volume of a cylinder....\n");
    printf("Enter the height of the cylinder:");
    scanf("%f", &h);
    v=PI*r*r*h;
    printf("the volume of the cylinder is %.2f", v);
    return 0;
}