#include<stdio.h>
int main()
{
	int a[13]={2,4,9,16,24,25,33,44,58,60,71,73,89};
	int n,first=0,last=12,mid;
	printf("请输入一个正整数：\n");
	scanf("%d",&n);
	while(first<=last)
	{
		mid=(int)(first+last)/2;
		if(n>a[mid])
			first=mid+1;
		else if(n<a[mid])
			last=mid-1;
		else
		{
			printf("该数在数组第%d位。\n",mid+1);
		    break;
		}
	}
	if(n!=a[mid])
	printf("查无此数\n");
	return 0;
}