#include <iostream>
#include <stdio.h>
#include <conio.h>

using namespace std;

int main()
{
    int a[100],n,i,c;
    printf("Enter number of integers");
    scanf("%d",&n);
    printf("enter %d integers\n",n);
    for(i=0;i<n;i++)
    {
        scanf("%d",&a[i]);
    }
    printf("enter the number to be searched");
    scanf("%d",&c);
    for(i=0;i<n;i++)
    {
      if(a[i]==c)
      {
        printf("%d is present at %d,\n",c,i+1);
        break;
      }
    }
    if(i==n)
    {

        printf("%d is not present,\n",c);
        return 0;
    }


}
