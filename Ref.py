#!/usr/bin/python
# -*- coding: utf-8 -*-
# from yahoo_finance import Currency

def findVendorNames(urls):
	vendorNames = []
	for country in countryAndURLsMap:
		urls = countryAndURLsMap[country]
		for url in urls:
			start = url.find('www.')
			
			#to add other domain extensions
			end = url.find('.com')
			if end == -1:
				end = url.find('.net')

			name = url[start+4:end]
			vendorNames.append(name)

	return vendorNames
# print findNames(urls)

currentCountry = "SG"
operatingCountries = {'SG':['Singapore', 'SGD']}
countryAndURLsMap = {'SG':["http://www.mustafa.com.sg/mmsnew/forex.aspx","http://www.raffles1.net/currency.php"]}#, "http://www.yakadir.com"]} #links MUST have www.
# countryAndURLsMap = {'SG': ["http://www.yakadir.com"]}
countryURLs = countryAndURLsMap[currentCountry]

vendors = findVendorNames(countryAndURLsMap)
# print vendors

#this is to map isos to corresponding country, currency names and symbols
countryInfoMap = {'USD': ['US', 'US Dollar (US$)'], 'TWD': ['TW', 'Taiwan Dollar (NT$)'], 'QAR': ['QA', 'Qatari Riyal (QR)'], \
				'EGP': ['EG', 'Egyptian Pound (ج.م)'], 'IDR': ['ID', 'Indonesian Rupiah (Rp)'], 'AED': ['AE', 'United Arab Emirates Dirham (د.إ)'], \
				'GBP': ['GB', 'British Pound (£)'], 'LKR': ["LK","Sri Lankan Rupee (Rs)"], 'DKK': ['DK', 'Danish Krona (Kr)'], \
				'CAD': ['CA', 'Canadian Dollar (C$)'], 'PKR': ["PK","Pakistani Rupee (Rs.)"], 'VND': ['VN', 'Vietnamese Dong (₫)'], \
				'KWD': ["KW","Kuwaiti Dinar (KWD)"], 'MYR': ['MY', 'Malaysian Ringgit (RM)'], 'MUR': ["MU","Mauritian Rupee (Rs)"], \
				'JOD': ["JO","Jordanian dinar (JOD)"], 'SAR': ['SA', 'Saudi Riyal (SR)'], 'UAE': ["AE","United Arab Emirates Dirham (د.إ)"], \
				'HKD': ['HK', 'Hong Kong Dollar (HK$)'], 'AUD': ['AU', 'Australian Dollar (A$)'], \
				'CHF': ['CH', 'Swiss Franc (Fr.)'], 'KRW': ['KR', 'South Korean Won (W)'], \
				'CNY': ['CN', 'Chinese Renminbi (¥)'], 'NZD': ['NZ', 'New-Zealand Dollar (NZ$)'], \
				'THB': ['TH', 'Thai Baht (฿)'], 'EUR': ['EU', 'Euro (€)'], 'NOK': ['NO', 'Norwegian Krona (kr)'], \
				'SEK': ['SE', 'Swedish Krona (kr)'], 'BHD': ["BH","Bahraini Dinar (د.ب)"], 'INR': ['IN', 'Indian Rupee (₹)'], \
				'JPY': ['JP', 'Japanese Yen (¥)'], 'OMR': ["OM","Omani Rial (بيسة)"], 'PHP': ['PH', 'Philippines Peso (₱)'], \
				'ZAR': ['ZA', 'South African Rand (R)'], 'SGD': ['SG', 'Singapore Dollar (S$)'], 'TRY': ['TR', 'Turkish Lira (₺)']}

#this is to map various(spelling errors included) currency names to one ISO.
currencyOntology = {'USD': ['US Dollars', 'AMERICAN DOLLARS'], 'EUR': ['EUROS'], 'GBP': ['BRITISH POUNDS', 'POUNDS'], 'TWD': ['Taiwan Dollars'], \
					'AUD': ['Australian Dollars'], 'CHF': ['Swiss Francs'], 'NZD': ['New Zealand Dollars'], \
					'CAD': ['Canadian Dollars'], 'JPY': ['Japanese Yen'], 'HKD': ['HONGKONG DOLLARS'], \
					'CNY': ['Chinese renminbi'], 'MYR': ['MALAYSIAN RINGGIT'], 'THB': ['THAI BAHT', 'THAILAND BAHT', 'THAI BHAT'], \
					'IDR': ['INDONESIAN RUPIAH'], 'PHP': ['PHILIPPINES PESO'], 'INR': ['INDIAN RUPEES'], \
					'SAR': ['SAUDI ARABIAN RIYALS'], 'KRW': ['SOUTH KOREAN WON'], 'UAE': ['UNITED ARAB EMIRATES'], \
					'TRY': ['TURKISH LIRAS'], 'SEK': ['SWEDISH KRONER', 'SWEDISH KRONA'], 'VND':['VIETNAM DONG'], 'LKR': ['SRI LANKAN RUPEE']}


def getISO(text):
	for iso in currencyOntology:
		for val in currencyOntology[iso]:
			if text.upper() in val.upper():
				return iso
	return None


usersCurrency = operatingCountries["SG"][1].upper()
	# iso = request.form["realCurrencySubmit"].upper()
