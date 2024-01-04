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
}in[TOTAL];//把老师和学生相同信息定义，不同放在共用体
int main()
{
	int i;
	printf("===========input information==========\n");//输入信息
	for(i=0;i<TOTAL;i++)
	{
		printf("name num sex(f/m) profession(s/t)\n");
		scanf("%s %d %s %s",in[i].name,&in[i].num,&in[i].sex,&in[i].profession);
		if(in[i].profession=='s'){
			printf("score\n");
			scanf("%lf",&in[i].sc.score);}
		else if(in[i].profession=='t'){
			printf("course\n");
			scanf("%s",in[i].sc.course);}//判断老师还是学生
	fflush(stdin);//清空缓冲区
	}
	printf("===========output information==========");//隔开
	printf("\nName\t\tNum\tSex\tProfession\tScore/Course\n");//输出信息
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
	return 0;//结束程序，返回0.
}