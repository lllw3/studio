#include<stdio.h>
int main()
{
	char c;
	int letters=0,spaces=0,digits=0,others=0;
	printf("please inrut a line of string:\n");
	while((c=getchar())!='\n')
	{
		if((c>='a'&&c<='z')||(c>='A'&&c<='Z'))
			letters++;
		else if(c>='0'&&c<='9')
			digits++;
		else if(c==' ')
			spaces++;
		else
			others++;
	}
	printf("there are %d letter.there are %d number.there are %d spaces.and there are %d others.\n",letters,digits,spaces,others);
	return 0;
}