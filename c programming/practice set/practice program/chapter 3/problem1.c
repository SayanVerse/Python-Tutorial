/*• 2. Write a program to determine whether a student has passed or
failed. To pass, a student requires a total of 40% and at least 33%
in each subject. Assume there are three subjects and take the
marks as input from the user. */

#include <stdio.h>

int main()
{
    int b, e, m, total;
    printf("ENter the marks in benglai:");
    scanf("%d", &b);
    printf("Enter the marks in english:");
    scanf("%d", e);
    printf("Enter the marks in math:");
    scanf("%d", &m);
    total=(b+e+m)/3;
    if((b<33 || e<33 || m<33) || total<33){
        printf("The student has failed in the exam!");
    }else{
        printf("The student has passed!");
    }

    return 0;
}