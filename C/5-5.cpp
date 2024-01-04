#include<stdio.h>
int main()
{
    int i,j,k;//i,j,k分别表示公鸡母鸡小鸡只数
	printf("百元买百鸡购买方法如下：\n");
    for(i=0;i<=100;i++)
         {
             for(j=0;j<=100;j++)
                  {
                       for(k=0;k<=100;k++)
					   {
						   if((k%3==0)&&(5*i+j*3+k/3==100)&&(i+j+k==100))
                           printf("公鸡：%d只，母鸡：%d只，小鸡：%d只\n",i,j,k);
					   }
                  }
          }
    return 0;
}