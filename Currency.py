class Currency(object):
	iso = ""
	name = ""
	units = ""
	buying = ""
	selling = ""
	vendor = ""
	available = True

	def __init__(self, iso, name, units, buying, selling, vendor=None):
		if vendor is None:
			self.iso = iso
			self.available = False
		else:
			self.iso = iso
			self.name = name
			self.units = units
			self.buying = buying
			self.selling = selling
			self.vendor = vendor


	def __eq__(self, other):
		# return self.iso is other.iso and self.name is other.name and self.units is other.units and self.buying is other.buying and self.selling is other.selling
		return self.iso == other.iso and self.name == other.name and self.units == other.units and self.buying == other.buying and self.selling == other.selling and self.vendor == other.vendor
	# def __hash__(self):
	# 	return hash(self.iso) and hash(self.name) and hash(self.units) and hash(self.buying) and hash(self.selling)

	# def __repr__(self):
		# return str(self.iso) + str(self.name) + str(self.units) + str(self.buying) + str(self.selling)

	# def __ne__(self,other):
	# 	if __eq__(self,other) == False:
	# 		return False
	# 	else:
	# 		return True

	# def __lt__(self,other):
	# 	return 
