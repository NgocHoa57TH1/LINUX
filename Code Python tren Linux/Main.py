from HCN import HCN
#Nhap ds N hinh hoc
n = int(input( "Nhap so luong HCN ban muon: "))
h = []
for i in range (0, n):
	ten = raw_input (" nhap ten: ")
	dai = int(input ("chieu dai: "))
	rong = int(input ("chieu rong: "))
	CN = HCN(dai, rong, ten)
	h.append(CN)
#in ra DT va CV cac hinh
for item in h:
	print "-------------------------------"
	cv = item.getChuVi()
	dt = item.getDienTich()
	print (item.toString())
	print ("Chu vi la " + str(cv) +"\n" + "Dien tich la " + str(dt))
#cho biet ten hcn co dien tich lon nhat
dt_max = h[0].getDienTich()
ten_max = h[0].getTen()
for item in h:
	if (dt_max < item.getDienTich()):
		dt_max = item.getDienTich()
		ten_max = item.getTen()
print ("HCN co dien tich lon nhat la " + ten_max + "co dien tich" + str(ten_max))
c = open
