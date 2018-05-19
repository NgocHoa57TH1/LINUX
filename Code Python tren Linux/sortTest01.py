#in ra day vua nhap
n = int(input("nhap n = "))
a=[]
for i in range(n):
	a.append(input ("nhap phan tu thu %d: " %(i+1)))
print (a)
#in ra phan tu chan
for i in range(n):
	if(a[i]%2 ==0):
		print (a[i])
#sx day va in
a.sort()
print (a)
#ghi vao file ten dia
fileData = open("OS.txt","w+")
for item in a:
	fileData.write(str(item))
	fileData.write("\n")
