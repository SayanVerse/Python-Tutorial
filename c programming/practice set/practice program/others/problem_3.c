//factorial programme using do while loop

#include <stdio.h>

int main(){
    int a;
    printf("Enter the number:");
    scanf("%d",&a);

    int factorial = 1;
    int i=1;

    do
    {
        factorial=factorial * i;
        i++;
    } while (i<=a);

    printf("The factorial of the number  is : %d", factorial);
    
    return 0;
}