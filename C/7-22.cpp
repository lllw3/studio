#include<stdio.h>
void sx(int c[]);
int main()
{
	int i,j,k,a[5]={46,27,15,10,5},b[8]={50,45,42,29,15,8,5,2};
	int c[13];
	j=0,k=0;
	for(i=0;i<13;i++)
	{
		if(j<5)
			c[i]=a[j++];
		else
			c[i]=b[k++];
	}
	printf("数组a和数组b整理排序得到的数组为：\n");
	sx(c);
	for(i=0;i<13;i++)
		printf("%d ",c[i]);
	printf("\n");
	return 0;
}
void sx(int c[])
{
	int i,j,t;
	for(i=1;i<=13;i++)
		for(j=0;j<=13-i;j++)
			if(c[j]>c[j+1])
			{
				t=c[j];
				c[j]=c[j+1];
				c[j+1]=t;
			}
}