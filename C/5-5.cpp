#include<stdio.h>
int main()
{
    int i,j,k;//i,j,k�ֱ��ʾ����ĸ��С��ֻ��
	printf("��Ԫ��ټ����򷽷����£�\n");
    for(i=0;i<=100;i++)
         {
             for(j=0;j<=100;j++)
                  {
                       for(k=0;k<=100;k++)
					   {
						   if((k%3==0)&&(5*i+j*3+k/3==100)&&(i+j+k==100))
                           printf("������%dֻ��ĸ����%dֻ��С����%dֻ\n",i,j,k);
					   }
                  }
          }
    return 0;
}