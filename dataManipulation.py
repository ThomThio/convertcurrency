import extractFromSite
import Ref
import ccy
import Currency
from OrderedDefaultDict import OrderedDefaultDict as ODD

vendors = Ref.vendors

#get all currency data to appear in the same tables, leave blank if not available
def mapAllCurrencies():
	mapping = extractFromSite.mapping
	# print mapping

	# c = Currency.Currency("USD", "US Dollar", "1", "1.5", "1.6", "Thomas Exchange")
	# mapping["Thomas Exchange"] = {c}
	# mapping["Joseph Exchange"] = {c}
	# mapping["Thio Exchange"] = {c}
	# vendors.append("Thomas Exchange")
	# vendors.append("Joseph Exchange")
	# vendors.append("Thio Exchange")

	currenciesWide = ODD(lambda: ODD()) #initializing
	for vendor in vendors:
		# print "\n" + str(vendor) + "\n"
		cList = []
		try:
			cList = sorted(mapping[vendor]) #sorts each currency list of every vendor in alphabetical order
		except:
			print "Exception occured"
			# cList = mapping[vendor]
			continue

		for obj in cList:
			iso = obj.iso

			if iso in currenciesWide.keys(): #if a currency of this acronym exists, add it to the existing list
				currenciesWide[iso][obj.vendor] = obj
				# print vars(obj)

			else: #if there are no currencies of this acronym yet, add an empty list, add the currency obj to that, and add it to the map
				
				# print vars(obj)
				currenciesWide[iso] = {}
				currenciesWide[iso][obj.vendor] = obj

	#populate missing currencies that other vendors do not cover with empty Currency objects
	for vendor in vendors:
		for iso in currenciesWide:
			try:
				currenciesWide[iso][vendor]
					# c = Currency.Currency(iso, None, None, None, None, None)
					# currenciesWide[iso][vendor] = c
			except KeyError: #to catch none objects
					c = Currency.Currency(iso, None, None, None, None, None)
					currenciesWide[iso][vendor] = c
					# print vars(c)

	# print len(currenciesWide)
	return currenciesWide


currenciesWide = mapAllCurrencies()
# print currenciesWide['IDR']