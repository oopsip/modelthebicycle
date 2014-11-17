
#Import your classes from a separate file
class Bicycle(object):
	#constructor methods- instantiation
	def __init__(self, modelname, weight, cost):
		self.modelname = modelname
		self.weight = weight
		self.cost = cost

	def initial(self):
		return self.modelname[0]

class Bikeshops(object):
	def __init__ (self,shopname, currentinventory):
		self.shopname = shopname
		self.currentinventory = currentinventory
		#self.margin = margin
		#self.profit = profilt
	def sellprice(self, product):
		return product.cost*1.2

	def profit(self, product):
	    return product.cost*0.2

class Customers(object):
	def __init__ (self, custname, fund):
		self.custname = custname
		self.fund = fund
	
	
