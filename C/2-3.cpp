#include<stdio.h>
/*������ų���PI ֵΪ3.1416*/
#define PI 3.1416
int main()
{
   printf("������Բ�ΰ뾶�����س�����");
   float radius,area,girth;
   scanf("%f",&radius);
   area=PI*radius*radius;//Բ�����
   girth=2*PI*radius;//Բ���ܳ�
   printf("the area is%f\n",area);
   printf("the girth is%f\n",girth);
   return 0;//�������
}