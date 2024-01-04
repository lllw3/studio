#include<stdlib.h>
#include<stdio.h>
#include<time.h>
int rNumber();
int rNumber()
{
	int number;
	srand(time(NULL));
	number=1+(rand()%100);
	return number;
}
void main()
{
	int a,number,i;
	printf("-----guess number----\n");
	number=rNumber();
	printf("game stsrt!\n");
	printf("\n");
	for(i=1;i<=8;i++)
	{
		printf("This are %d guesses,please input the number,press enter to end:",i);
		scanf("%d",&a);
		if(a>number)
			printf("that is too big!\n");
		else if(a<number)
			printf("that is too small!\n");
		else if(a=number)
			printf("you are right!congratulation!games over\n");break;
	}
	if(i>8)
		printf("sorry,you are lost!games over!");
}
