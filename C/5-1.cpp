#include<stdio.h>
int main()
{
    int i=1,sum=0;//�������α���i��sum����ʼ��
    while(i<=100)//���ʽ����������ѭ��
        {
           sum=sum+i*i;
           i++;
        }
    printf("1^2+2^2+3^2+...+100^2=%d",sum);//�����ͽ��
    return 0;
}