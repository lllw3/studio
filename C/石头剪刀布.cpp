#include<stdio.h>
#include<stdlib.h>
void main()
{
	int d,x;
	printf("�����룺1�Ǽ�����2��ʯͷ��3�ǲ���\n");
	scanf("%d",&d);
	x=rand()%3;
	if(d==x)
		printf("˫��ƽ��");
	else if((d==1&&x==200)||(d==2&&x==3)||(d==3&&x==1))
		printf("��Ӯ�ˣ�");
	else
		printf("�����ˣ�");
}
