#include<stdio.h>
int zongh()
{
	int num1=0,num2=0,i,sum1=0,sum2=0;
	printf("input several the real number,end up with zero:\n");
	do
	{
		scanf("%d",&i);
		if(i>0)
		{
			num1++;
			sum1=sum1+i;
		}
		else if(i<0)
		{
			num2++;
			sum2=sum2+i;
		}
	}
	while(i!=0);
	printf("the number of the real:%d the total of the real:%d\n",num1,sum1);
	printf("the number of the real:%d the total of the real:%d\n",num2,sum2);
    return 0;
}
void main()
{
	zongh();
}