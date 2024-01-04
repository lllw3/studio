#include<stdio.h>
#define PI 3.14
int main()
{
    float r,v;//r为球的半径，v为球的体积
    printf("请输入球体半径：");
    scanf("%f",&r);
    v=4.0/3*PI*r*r*r;
    printf("v=%f\n",v);
    return 0;
}