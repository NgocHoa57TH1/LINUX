#include<stdio.h>
int mu(int a,int b)
{
     if(b==1)
     return a;
     else
     return mu(a,b-1)*a;
}
     
int main()
{
    int n,x;
    printf("nhap co so n nao:  ");
    scanf("%d",&n);
    printf("tiep theo nhap so mu:  ");
    scanf("%d",&x);
    printf("dap an day nay: %d\n",mu(n,x));
   
}
