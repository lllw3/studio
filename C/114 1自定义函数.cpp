#include<stdio.h>
int gose()
{
	int i,n,sum=0;
	scanf("%d",&n);
	for(i=1;i<=n;i++)
	{
		sum+=i*i;
	}
	printf("1^2+2^2+...%d^2=",n);
	printf("%d\n",sum);
	return sum;
}
int main()
{
	printf("ÇëÊäÈënÖµ:");
	gose();
	return 0;
}