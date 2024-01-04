#include<stdio.h>
int main()
{
	int n,i,j,a[100];
	n=10;
	printf("    1");
	printf("\n");
	a[1]=a[2]=1;
	printf("%5d%5d\n",a[1],a[2]);
	for(i=3;i<=n;i++)
	{
		a[1]=a[i]=1;
		for(j=i-1;j>1;j--)
			a[j]=a[j]+a[j-1];
		for(j=1;j<=i;j++)
			printf("%5d",a[j]);
		printf("\n");
	}
 	return 0;
}