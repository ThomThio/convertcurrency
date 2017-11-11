#!/usr/bin/python
# -*- coding: utf-8 -*-
import lxml
# import bs4.builder._lxml
import requests
import bs4
import Ref
from Currency import Currency
import urllib2
# The standard library modules
import os
import sys

# The wget module
# import wget


# The selenium module
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By

# import jabba_webkit as jw

from collections import OrderedDict

uList = Ref.countryURLs
mapping = OrderedDict()



#add scraping methods
def scrapeAllSites(): 
	# getCurrencyData_ajax()
	getCurrencyData()
	


def check(val):
	blacklist = ["convert this amount", "code,", "is code", "currency", "currency name", "units", "buying rate", "selling rate", "selling", "buying", "\xc2\xa0"] #add unnecessary values to filter out here. upper/lower case does not matter
	# print "conducting check"
	if val is not None:
		if isinstance(val, unicode) and len(val) > 0:
			val =  val.encode('utf8')
			if val.upper().lower() in blacklist:
				# print "removed:", val
				return None
			else:
				# print val
				return val
		elif isinstance(val, unicode) and len(val) == 0:
			# print "Blank found!"
			return None


		elif isinstance(val, str) and len(val) > 0: #remove unnecessary values here
			if val.upper().lower() in blacklist:
				# print "removed:", val
				return None
			else:
				# print val
				return val
		
		elif isinstance(val, str) and len(val) == 0:
			# print "Blank found!"
			return None
	else:
		# print val
		return None

#getting data for dynamic ajax pages
def getCurrencyData_ajax():
	for url in uList:
		currenciesForSite = []

		if "yakadir" in url: #21 currencies

			# display =Display(visible=1, size=(320, 240)).start()
			# display.start()
			# driver = webdriver.Firefox() # if you want to use chrome, replace Firefox() with Chrome()
			# driver.get(url)
			# WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "newsboxin")))
			
			page = ""
			# try:
			# page = jw.get_page(url, 15)
			# except:
				# return None
			# display.stop()

			# print page
			soup = bs4.BeautifulSoup(page, "lxml")
			# print soup
			

			#yakadir has grey/white divs
			colList = ['grey', 'white']

			for col in colList:
				colors = soup.findAll('div', col)
				for divClasses in colors:
					name = None
					buying = None
					selling = None

					#rows is a list of the the divs/column data
					rows = divClasses.find_all("div")

					name = check(rows[0].find(text=True))
					buying = check(rows[1].find(text=True))
					selling = check(rows[2].find(text=True))

					if name and buying and selling is not None:
					# 	#yakadir has no iso, we use Ref library to get it
						iso = Ref.getISO(name[0:5]) #takes a substring of name, to prevent weird characters at the end from entering
						if iso is None:
							print ("Unrecognized iso. Check Ref for: " + name)

						name = Ref.countryInfoMap[iso][1]
						units = "NA" #yakadir uses strange denominations

						c = Currency(iso,name,units,buying,selling,"yakadir")
						# print vars(c)
					else:
						pass

					currenciesForSite.append(c)
				mapping["yakadir"] = currenciesForSite
			# driver.quit()

		currenciesForSite = [] #resets at end of for loop of urls
	
	
	return mapping

# map1 = getCurrencyData_ajax()
# print map1["yakadir"]

#getting data directly - no ajax or hidden forms.
def getCurrencyData():
	for url in uList:
		page = requests.get(url)
		soup = bs4.BeautifulSoup(page.content)
		currenciesForSite = []
		for tr in soup.findAll('tr'):
			rows = tr.findAll('td')

			if "raffles1" in url and len(rows) == 5:
				iso = check(rows[0].find(text=True))
				name = check(rows[1].find(text=True))
				units = check(rows[2].find(text=True))
				selling = check(rows[3].find(text=True)) #raffles site puts selling first
				buying = check(rows[4].find(text=True))

				if iso and name and units and selling and buying is not None:
					c = Currency(iso,name,units,buying,selling,"raffles1")
					currenciesForSite.append(c)
					# print iso,name,units,selling,buying
					# print vars(c)
				else:
					pass
				mapping["raffles1"] = currenciesForSite		


			elif "mustafa" in url and len(rows) == 7:
				iso = check(rows[2].find(text=True))
				name = check(rows[3].find(text=True))
				units = check(rows[4].find(text=True))
				buying = check(rows[5].find(text=True)) #mustafa site puts buying first
				selling = check(rows[6].find(text=True))

				if iso and name and units and selling and buying is not None:
					c = Currency(iso,name,units,buying,selling,"mustafa")
					currenciesForSite.append(c)
					# print iso,name,units,selling,buying #use these to check for unwanted values that went through
					# print vars(c)
				else:
					pass
				mapping["mustafa"] = currenciesForSite
		
		currenciesForSite = []
	# print len(mapping["raffles1"])
	# print len(mapping["mustafa"])

	#remove duplicates
	# for site in mapping:
		# newList = []
		# print site.upper() + "\n"
		# newList = removeDuplicates(mapping[site])
		# print len(mapping[site])

		# mapping[site] = newList
		# print len(newList)
		# for cObj in newList:
		# 	print vars(cObj)
	return mapping


def removeDuplicates(original_list):
	#removes header and duplicates of the header
	if len(original_list) > 0:

		check = original_list[0]
		output = []
		for x in original_list:
			if check.units == x.units:
				original_list.remove(x)
				# output.append(x)
			elif (x.iso, x.name, x.units, x.buying, x.selling) is None:
				original_list.remove(x)

		return original_list
	else:
		return []

scrapeAllSites()
# getCurrencyData()
