#include<stdio.h>
void ss()
{
	int i,n,count=0;
	printf("请输入n值：");
	scanf("%d",&n);
	printf("输出1-%d中能被3和5同时整除的整数：\n",n);
	for(i=1;i<=n;i++)
	{
		if(i%3==0&&i%5==0){
			printf("%4d",i);
			count++;
			if(count%6==0)
				printf("\n");
		}
	}
}
int main()
{
	ss();
	return 0;
}