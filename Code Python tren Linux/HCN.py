class HCN:
	dai = 0
	rong = 0
	ten =""
	def __init__ (self, dai, rong,ten):
		self.dai = dai
		self.rong = rong
		self.ten = ten
	def toString(self):
		return "HCN" + self.ten + "(" + str(self.dai) + "," + str(self.rong) + ")"
	def getChuVi(self):
		return (self.dai + self.rong)*2
	def getDienTich(self):
		return self.dai * self.rong

