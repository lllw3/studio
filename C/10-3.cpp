#include<stdio.h>
int main()
{
	int date;
	enum weekday{sun=7,mon=1,tue,wed, thu,fri,sat}day;//����ö�����ͣ�����һ�������գ�
	printf("enter weekday number(1-7)\n");
	scanf("%d",&date);//�����Ӧ����
	day=(enum weekday)date;//ǿ�ư�����ת�����и�ֵ
	switch(day)
	{
	case sun:printf("weekday is sun.");break;
	case mon:printf("weekday is mon.");break;
	case tue:printf("weekday is tue.");break;
	case wed:printf("weekday is wed.");break;
	case thu:printf("weekday is thu.");break;
	case fri:printf("weekday is fri.");break;
	case sat:printf("weekday is sat.");break;
	default:printf("error!!");break;
	}
	printf("\n");
	return 0;
}