#include "iostream"
#include "windows.h"
using namespace std;
 
unsigned int prime(unsigned int lmax)
{
    bool* prime_num = new bool[lmax];
    memset(prime_num, true, sizeof(bool) * lmax);
 
    for (unsigned int i = 2; i < lmax; ++i)
    {
        if (prime_num[i])
            for (unsigned int j = 2; i * j < lmax; ++j)
                prime_num[i * j] = false;
    }
 
    unsigned int pnum = 0;
    for (unsigned int i = 2; i < lmax; ++i)
    {
        if (prime_num[i])
            ++pnum;
    }
 
    delete[] prime_num;
    return pnum;
}
 
int main()
{
    int a = 100;
    DWORD s = GetTickCount();
    unsigned int pnum = prime(100);
    float use_time = ((float)(GetTickCount() - s)) / 1000.f;
 
    cout<<"100 以内有素数个数 : "<<pnum<<endl;
    cout<<"用时 : "<<use_time<<"秒"<<endl;
 
 
    return 0;
}
