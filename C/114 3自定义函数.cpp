#include<stdio.h>
void ss()
{
	int i,n,count=0;
	printf("������nֵ��");
	scanf("%d",&n);
	printf("���1-%d���ܱ�3��5ͬʱ������������\n",n);
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