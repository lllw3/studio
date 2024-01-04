#include<stdio.h>
int main()
{
	int a,b;
	char c;
    printf("«Î ‰»Î:x'+'x\n");
	while((scanf("%d%c%d",&a,&c,&b))==3)
	{
		switch(c)
		{
		    case'-':printf("%d-%d=%d\t\n",a,b,a-b);break;
			case'+':printf("%d+%d=%d\t\n",a,b,a+b);break;
			case'*':printf("%d*%d=%d\t\n",a,b,a*b);break;
			case'/':printf("%d/%d=%f\t\n",a,b,(float)a/b);break;
			default:printf(" ‰»Î¥ÌŒÛ!\n");
		}
	printf("«Î ‰»Îx'+'x\n");
	}
	return 0;
}
