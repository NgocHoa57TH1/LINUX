#include<stdio.h>
int main()
{
	int s=0;int n;
	printf(" nhap so ban thich nao: ");
	scanf("%d",&n);
	for (int i = 2; i<=n; i+=2)
		s+=i;
	printf(" Tong chan la: %d\n",s);
	
	
}
