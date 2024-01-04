#include <stdio.h>
int main()
{
   /*声明变量*/
   int a,b;
   unsigned int u;
   long L;
   char ch;
      float f;

     /*变量赋值*/
     a=200;
     b=-1;
     u=b;
     L=u;
     ch='A';
     f=32.17;
     
     /*输出*/
     printf("a=%d\t",a);
     printf("b=%d\n",b);
     printf("u=%u\t",u);
     printf("L=%ld\n",L);
     printf("f=%f\n",f);
     printf("ch is %c and value is %d\n",ch,ch);
     printf("I love C language!\rYou\n");
}