#include<stdio.h>
int main()
{
   float x,y,ans;
   int n;
   printf("������2����������\n");
   scanf("%f,%f",&x,&y);
   ans=x/y;
   n=(int)(ans*100)%10;
   printf("��Ϊ��%f���̵ĵڶ�λС����%d\n",ans,n);
   return 0;
}