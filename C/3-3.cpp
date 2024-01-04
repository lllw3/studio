#include<stdio.h>
int main()
{
   float x,y,ans;
   int n;
   printf("请输入2个浮点数：\n");
   scanf("%f,%f",&x,&y);
   ans=x/y;
   n=(int)(ans*100)%10;
   printf("商为：%f，商的第二位小数：%d\n",ans,n);
   return 0;
}