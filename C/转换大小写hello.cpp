#include<stdio.h>
#define LETIER 1 
int main()
{
	char str[20]="Hello",c;
	int i;
	i=0;
	while((c=str[i])!='\0')
	{
		i++;
#if LETIER
		if(c>='a'&&c<='z')
			c=c-32;
#else
		if(c>='A'&&c<='Z')
			c=c+32;
#endif
		printf("%c",c);
	}
	printf("\n");
	return 0;
}