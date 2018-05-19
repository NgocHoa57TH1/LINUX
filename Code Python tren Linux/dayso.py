n = int(input(" nhap vao mot so x bat ki 0<x<10:"))
arr = []
for i in range (0,n):
	arr.append(i+1)
print (arr)
sum = 0
for i in range (n):
	if (arr[i] % 2 == 0):
		sum = sum + arr[i]
print "tong so chan: %d" %(sum)
	
