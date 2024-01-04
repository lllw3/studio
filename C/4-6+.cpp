#include<stdio.h>
int main()
{
     int e,m,s,d,t;//e为基本运费，m为重量，s为距离，d为折扣，t为总运费
     printf("请输入距离s:\n");
     scanf("%d",&s);
     if(s<200)
       d=0;//不打折情况
     else if(s>=200&&s<600)
       d=3;//折扣为3%情况
     else if(s>=600&&s<1000)
       d=6;//折扣为6%情况
     else if(s>=1000&&s<2000) 
       d=9;//折扣为9%情况
     else if(s>=2000)
       d=11;//折扣为11%情况
	 t=e*m*s*(1-d/100);
     printf("总运费t为%d元",t);//输出运费
     return 0;//结束程序
}