#include<stdio.h>
int main()
{
    int num;
    printf("������һ�����������س�������");
    scanf("%d",&num);
    if(num%2==0&&num%3==0)
    printf("%d���Ա�2,3����",num);
    else
    printf("%d�����Ա�2,3����",num);
    return 0;
}