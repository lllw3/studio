#include<stdio.h>
int main()
{
	int a,b;
	char c;
    printf("������:x'+'x\n");
	while((scanf("%d%c%d",&a,&c,&b))==3)
	{
		switch(c)
		{
		    case'-':printf("%d-%d=%d\t\n",a,b,a-b);break;
			case'+':printf("%d+%d=%d\t\n",a,b,a+b);break;
			case'*':printf("%d*%d=%d\t\n",a,b,a*b);break;
			case'/':printf("%d/%d=%f\t\n",a,b,(float)a/b);break;
			default:printf("�������!\n");
		}
	printf("������x'+'x\n");
	}
	return 0;
}
