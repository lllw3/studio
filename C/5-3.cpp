#include<stdio.h>
int main()
{
     int n,c=0;
     for(n=1;n>=1&&n<=200;n++)
           {
                if(n%3==0&&n%5==0)
                   {
                       printf("%d ",n);
                       c++;
                       if(c%6==0)
                       printf("\n");
                    }
           }
      printf("\n");
      return 0;
}