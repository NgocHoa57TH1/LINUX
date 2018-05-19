class Sinhvien:
	def __init__(self,mssv,hoten,makhoa):
		self.mssv=mssv
		self.hoten=hoten
		self.makhoa=makhoa
	def setMSSV(self,mssv):
		self.mssv=mssv
	def setTen(self,ten):
		self.ten=ten
	def setMakhoa(self,makhoa):
		self.makhoa=makhoa
	def getMSSV(self):
		return self.mssv
	def getTen(self):
		return self.ten
	def getMakhoa(self):
		return self.makhoa
	def toString(self):
		print self.mssv," - ",self.hoten," - ",self.makhoa
