#4.1
from Sinhvien import *
from khoa import *
#nhapdssv
print "--------danh sach sinh vien-------"
listsv=[]
sv=Sinhvien("001","Mai A","01")
listsv.append(sv)
sv=Sinhvien("002","Tran B","01")
listsv.append(sv)
sv=Sinhvien("003","Van C","02")
listsv.append(sv)
sv=Sinhvien("004","Thi K","001")
listsv.append(sv)
#in dssv
size = len(listsv)
i=0
while i<size:
	listsv[i].toString()
	i=i+1
#nhap dsk
print "---------danh sach khoa--------"
listkhoa=[]
kh=Khoa("01","CNTT")
listkhoa.append(kh)
kh=Khoa("02","Ktoan")
listkhoa.append(kh)
kh=Khoa("03","Ckhi")
listkhoa.append(kh)
kh=Khoa("04","Nuoi")
listkhoa.append(kh)
#in dsk
size = len(listkhoa)
n=0
while n<size:
	listkhoa[n].toString()
	n=n+1
#4.2
size = len(listsv)
m=0
print "----danh sach sinh vien Khoa CNTT----"
while m<size:
	if listsv[m].getMakhoa()=="01":
		listsv[m].toString()
		m = m + 1
