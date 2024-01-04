#include<stdio.h>
int main()
{
	int a,b,c,d,e,f=0;
	printf("把一百元兑换的方案如下：\n");
	for(a=1;a<=2;a++)
		for(b=1;b<=5;b++)
			for(c=1;c<=10;c++)
				for(d=1;d<=20;d++)
					for(e=1;e<=100;e++)
				{
					if(50*a+20*b+10*c+5*d+e==100)
					{	
						f++;
					    printf("50元：%2d张，20元：%2d张，10元：%2d张，5元：%2d张，1元：%2d张\n",a,b,c,d,e);
					}
				}
    printf("共%d种方案",f);
    return 0;
}