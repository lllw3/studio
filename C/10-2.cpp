#include<stdio.h>
#include<stdlib.h>
#define TOTAL 2
struct{
   char name[20];
   int num;
   char sex;
   char profession;
   union{
     double score;
	 char course[20];
   }sc;
}in[TOTAL];//����ʦ��ѧ����ͬ��Ϣ���壬��ͬ���ڹ�����
int main()
{
	int i;
	printf("===========input information==========\n");//������Ϣ
	for(i=0;i<TOTAL;i++)
	{
		printf("name num sex(f/m) profession(s/t)\n");
		scanf("%s %d %s %s",in[i].name,&in[i].num,&in[i].sex,&in[i].profession);
		if(in[i].profession=='s'){
			printf("score\n");
			scanf("%lf",&in[i].sc.score);}
		else if(in[i].profession=='t'){
			printf("course\n");
			scanf("%s",in[i].sc.course);}//�ж���ʦ����ѧ��
	fflush(stdin);//��ջ�����
	}
	printf("===========output information==========");//����
	printf("\nName\t\tNum\tSex\tProfession\tScore/Course\n");//�����Ϣ
	for(i=0;i<TOTAL;i++)
	{
		if(in[i].profession=='s')
		{
			printf("%s\t%d\t%c\t%c\t\t%5.2lf\n",in[i].name,in[i].num,in[i].sex,in[i].profession,in[i].sc.score);
		}
		else if(in[i].profession=='t')
		{
			printf("%s\t%d\t%c\t%c\t\t%s\n",in[i].name,in[i].num,in[i].sex,in[i].profession,in[i].sc.course);
		}
	}
	return 0;//�������򣬷���0.
}