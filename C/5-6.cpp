#include<stdio.h>
int main()
{
	int a,b,c,d,e,f=0;
	printf("��һ��Ԫ�һ��ķ������£�\n");
	for(a=1;a<=2;a++)
		for(b=1;b<=5;b++)
			for(c=1;c<=10;c++)
				for(d=1;d<=20;d++)
					for(e=1;e<=100;e++)
				{
					if(50*a+20*b+10*c+5*d+e==100)
					{	
						f++;
					    printf("50Ԫ��%2d�ţ�20Ԫ��%2d�ţ�10Ԫ��%2d�ţ�5Ԫ��%2d�ţ�1Ԫ��%2d��\n",a,b,c,d,e);
					}
				}
    printf("��%d�ַ���",f);
    return 0;
}