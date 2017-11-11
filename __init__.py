from flask import Flask, render_template, Markup, flash, session, redirect, url_for, request
from app import extractFromSite
from app import dataManipulation
import Ref
import sys
reload(sys)
sys.setdefaultencoding('UTF-8')

#add site names here
vendors = Ref.vendors
country = "SG"
currenciesWide = dataManipulation.currenciesWide

app = Flask(__name__, static_url_path='')
app.static_folder = 'static'
wsgi_app = app.wsgi_app

#sample login function
def login_required(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return f(*args, **kwargs)
		else:
			flash('Please login/sign up first!')
			return redirect(url_for('/'))
	return wrap
#sample login function

def getHeaders():
	headers = "<th>Code</th><th>Currency</th>"
	units = "'s Units</th>"
	buysSellsAt = " Rates</th>"

	vendorHeader = ""

	 #standardizing order of columns of vendors by USD
	for vendor in currenciesWide['USD']:
		vendorHeader += "<th>" + vendor + units + "<th>" + vendor + buysSellsAt
    
	headers += vendorHeader
	return headers


def makeAndFilterCell(val):
	if val is None:
		return "<td>NA</td>"
	elif isinstance(val, str):
		return "<td>" + val + "</td>"
	elif isinstance(val, unicode):
		return "<td>" + val.encode('utf8') + "</td>"
	else:
		# return None
		return "<td>" + val.decode('utf-8') + "</td>"


@app.route("/", methods=['GET', 'POST'])
def populateView():
	headers = getHeaders()
	numVendors = len(Ref.vendors)
	numCurrencies = len(currenciesWide)
	orderedVendorList = []
	for vendor in currenciesWide['USD']:
		orderedVendorList.append(vendor)
	output = currencyOverview(orderedVendorList)

	#get map of country where user is accessing from
	mapIcon = "<span class='flag-icon flag-icon-" + country.lower() +"'></span>"

	return render_template('template.html', location=country, flag=mapIcon, headers=headers, output=output, numCurrencies=numCurrencies, numVendors=numVendors)
	
	# if request.form["realCurrencySubmit"] is n ot None:

	# 	usersCurrency = Ref.operatingCountries[country][1].upper()
	# 	iso = request.form["realCurrencySubmit"].upper()
	# 	realCurrencyPrice = Currency(usersCurrency+iso)
	# 	print realCurrencyPrice
	# 	print realCurrencyPrice.get_trade_datetime()

	# 	return render_template("template.html", realCurrencyPrice=realCurrencyPrice if success else "")


def currencyOverview(orderedVendorList):
	
	output = ""
	for iso in currenciesWide:
		vendorMap = currenciesWide[iso]
		stackedCells = ""

		countryCode = Ref.countryInfoMap[iso][0].lower() #to find png flag using country code
		if countryCode is not None:
				iso2 = makeAndFilterCell(iso + "<span class='flag-icon flag-icon-" + countryCode +"'></span>") #creates cell with currency code + flag
				# iso2 = "<th>" + iso + "<span class='flag-icon flag-icon-" + countryCode +"'></span></th>"
		else:
			countryCode = "xx"

			# out = "<html>%(head)s%(prologue)s%(query)s%(tail)s</html>" % locals(), out = "<html>%s%s%s%s</html>" % (head, prologue, query, tail)

		currencyName = Ref.countryInfoMap[iso][1]
		currencyName = makeAndFilterCell(currencyName)
		output += "<tr class='md-trigger md-setperspective' data-modal='modal-19' id='" + iso + "'>" + iso2 + currencyName


		
		for vendor in orderedVendorList:
			obj = vendorMap[vendor]
			
		# 	# print vars(obj)
			if obj.available is True:
			
		# 		# 	currencyName = currencyName + " (" + symbol + ")" #add currency symbol to currency name
				unitSpan = "<span id='units-" + vendor + "'>"  #to divide buying/selling by its units later for comparison with other rates
				units = unitSpan + obj.units + "</span>"
				unitOutput = makeAndFilterCell(units)

				buySpan = "<span id='buying-" + vendor + "'>"
				sellSpan = "<span id='selling-" + vendor + "'>"
				buyPrice = obj.buying
				sellPrice = obj.selling

				#check for buying/selling price below 0
				if buyPrice < 0.00000001:
					buyPrice = "NA"
				if sellPrice < 0.00000001:
					sellPrice = "NA"

				buyingSellingOutput = makeAndFilterCell("Buying: " + buySpan + buyPrice + "</span>" + "<br>" + "Selling: " + sellSpan + sellPrice + "</span>" + "<br>")
	 			# vendor = makeAndFilterCell(vendor)
				stackedCells = stackedCells + unitOutput + buyingSellingOutput
			
			elif obj.available is False:
				stackedCells += "<td>NA</td><td>NA</td>"
			
		output += stackedCells + "</tr>"
	return output #returns full html content

# populateView()

def generateTemplate():
	return render_template('index.html')

