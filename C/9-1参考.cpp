#include<stdio.h>
void max_min_change(int*n)
{
	int*max,*min,*p,t;
	max=min=n;
	for(p=n+1;p<n+10;p++)
		if(*p>*max)
			max=p;
		else if(*p<*min)
			min=p;
		t=n[9];
		n[9]=*min;
		*min=t;
		if(max==n)
			max=min;
		t=n[0];
		n[0]=*max;
		*max=t;

}
int main()
{
	int i,n[10],*p;
	printf("please input 10 numbers:\n");
	for(i=0;i<10;i++)
		scanf("%d",&n[i]);
	max_min_change(n);
	printf("after change,the arry is:\n");
	for(p=n;p<n+10;p++)
		printf("%2d",*p);
	printf("\n");
	return 0;
}