#include<stdio.h>
#include<math.h>
int main()
{
	int m,i,k;
	printf("输入一个数:");
	scanf("%d",&m);
	k=(int)sqrt((double)m);
	for(i=2;i<=k;i++)
		if(m%i==0)
			break;
		if(i<k)
			printf("%d是素数。\n",m);
		else
			printf("%d不是素数。\n",m);
	return 0;
}