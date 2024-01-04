/*有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），凡报到3的人退出
圈子，问最后留下的是原来第几号的那位。*/
#include<stdio.h>
#define nmax 50
int main()
{

	int i,k,m,n,num[nmax],*p;
	printf("please input the total of numbers:");
	scanf("%d",&n);
	p=num;
	for(i=0;i<n;i++)
		*(p+i)=i+1;
	i=0;
	k=0;
	m=0;
	while(m<n-1)
	{
		if(*(p+i)!=0) k++;
		if(k==3)
		{
			*(p+i)=0;
			k=0;
			m++;
		}
        i++;
		if(i==n)
			i=0;
	}
	while(*p==0)
		p++;
	printf("%d is left\n",*p);
	return 0;
}