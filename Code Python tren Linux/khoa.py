class Khoa:
	def __init__(self,makhoa,tenkhoa):
		self.makhoa=makhoa
		self.tenkhoa=tenkhoa
	def setMAKHOA(self,makhoa):
		self.makhoa=makhoa
	def setTENKHOA(self,tenkhoa):
		self.tenkhoa=tenkhoa
	def getMAKHOA(self):
		return self.makhoa
	def getTENKHOA(self):
		return self.tenkhoa
	def toString(self):
		print self.makhoa," - ",self.tenkhoa
