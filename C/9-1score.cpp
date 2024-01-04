#include<stdio.h>
#include<stdlib.h>
void fun(int *n)
{
	int*max,*min,*p,temp;
	max=min=n;
	for(p=a+1;p<a+10;p++)
	{
		if(*p>*max)
		max=p;
		else if(*p<*min)
		min=p;
	}
	temp=a[0];
	a[0]=*max;
	*max=temp;
	temp=a[9];
	a[9]=*min;
	*min=temp;
 } 
 int main()
 {
 	int a[10],*p;
 	for(p=a;p<a+10;p++)
 	scanf_s("%d",p);
	 fun(a) ;
	 for(p=a;p<a+10;p++)
	 *max=temp;
	 temp=a[9];
	 a[9]=*min;
	 *min=temp;
 }
 int main()
 {
 	int a[10],*p;
 	for(p=a;p<a+10;p++)
 	scanf_s("%d",p);
 	fun(a);
 	for(p=a;p<a+10;p++)
 	printf("%d",*p);
 	printf("\n");
	 system(pause);
	 return 0; 
 }
