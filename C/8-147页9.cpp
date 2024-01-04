#include<stdio.h>
void insert(int a[])
{
	int i,w;
	for(i=0;i<9;i++)
		scanf("%d",&a[i]);
	printf("\n");
	printf("请输入一个数字。");
    scanf("%d",&w);
	a[9]=w;
	for(i=8;i>=0;i--)
		if(w<a[i])
			a[i+1]=a[i];
		else{
			a[i+1]=w;
		    break;
		}
	printf("现在数组为：");
	for(i=0;i<10;i++)
		printf("%d ",a[i]);
	printf("\n");
}
int main()
{
	int a[10];
	printf("请由小到大输入9个数字。\n");
	insert(a);
	return 0;
}