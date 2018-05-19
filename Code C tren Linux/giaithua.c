#include<stdio.h>
int main(){  
  int i,giaithua=1,n;  
  
  printf("Nhap mot so bat ky: ");  
  scanf("%d",&n);  
  
  for(i=1;i<=n;i++){  
      giaithua=giaithua*i;  
  }  
  printf("\nGiai thua cua %d la: %d",n,giaithua);  
  
  printf("\n\n===========================\n");

}
