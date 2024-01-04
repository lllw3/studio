#include<stdio.h>
/*定义符号常量PI 值为3.1416*/
#define PI 3.1416
int main()
{
   printf("请输入圆形半径，按回车结束");
   float radius,area,girth;
   scanf("%f",&radius);
   area=PI*radius*radius;//圆形面积
   girth=2*PI*radius;//圆形周长
   printf("the area is%f\n",area);
   printf("the girth is%f\n",girth);
   return 0;//程序结束
}