#include<stdio.h>

/* Ham tinh giai thua */
int giaithua(int n)
{
 int gt = 1;
 for (int i = 1; i<=n; i++)
 	gt = gt * i;
 return gt;
}
/* ham tinh tong chan */
int tongchan(int n)
{
 int s = 0;
 for ( int i = 2; i <= n; i+=2)
	s+=i;
 return s;
}
/* ham tinh tong le */
int tongle(int n)
{
 int s = 0;
 for (int i = 1; i <= n; i+=2)
	s+=i;
 return s;
}
/* ham tinh luy thuy */
int luythua(int n,int x)
{
 if(x==1)
     return n;
     else
     return luythua(n,x-1)*n;
}
