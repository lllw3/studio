#include<stdio.h>
int main()
{
     int i,sum=0,m=0;//�������i��sum��m
     for(i=1;i<=9;i++)
     {
         m=m*10+i;
         sum=sum+m; 
     }
     printf("1+12+123+...123456789=%d",sum);//������
     return 0;
}