#include<stdio.h>
int main()
{
     int s,m,d,e,t,a;
     printf("please input the distance:\n");
     scanf("%d",&s);
     if(s<200)
        a=0;
     else if(s<=600&&s>=200)
         a=1;
     else if(s>600&&s<=1000)
         a=2;
     else if(s>1000&&s<=2000)
         a=3;
     else if(s>2000)
         a=4;
     switch(a)
     {
          case 0:t=e*m*s;break;
          case 1:d=3;t=e*m*s*(1-d/100);break;
          case 2:d=6;t=e*m*s*(1-d/100);break;
          case 3:d=9;t=e*m*s*(1-d/100);break;
          case 4:d=11;t=e*m*s*(1-d/100);break;
     }
     printf("the total cost:%d",t);
     return 0;
}
