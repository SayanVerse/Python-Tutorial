// write a c programme to calculate simple interest

#include <stdio.h>

int main(){
    float p,t,r;

    printf("Enter principle amount value:");
    scanf("%f",&p);

    printf("Enter interest rate:");
    scanf("%f",&r);

    printf("Enter time period in year:");
    scanf("%f",&t);

    float interest= (p*t*r)/3;

    printf("The interest is : %.2f", interest);


    return 0;
}