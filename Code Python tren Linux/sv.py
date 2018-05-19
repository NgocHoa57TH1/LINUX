class Sinhvien:
	def __int__(self,MSSV,Hoten,Makhoa):
		self.MSSV = MSSV
		self.Hoten = Hoten
		self.Moaakhoa = Makhoa
	def getMSSV(self)
		return self.MSSV
	def setMSSV(self, MSSV)
		self.MSSV = MSSV
	def getHoten(self)
		return self.Hoten
	def setHoten(self, Hoten)
		self.Hoten = Hoten
	def getMakhoa(self)
		return self.Makhoa
	def setMakhoa(self, Makhoa)
		self.Makhoa = Makhoa
	def toString(self):
		print self.MSSV," - ",self.Hoten," - ",self.Makhoa


