# -*- coding: utf-8 -*-
from BeautifulSoup import BeautifulSoup
#from bs4 import BeautifulSoup
import urllib2
import re
from datetime import datetime
import xlsxwriter
import requests
from nameparser import HumanName
 


#filters headlines to get only relevant content
headlineFilter = {"starts": 1, "adds": 1, "moving forward": 2, "in talks": 1, "to board":2, "boards":2, "teams up":1, 
"teams with":1, "reteams up": 1, "reteams with": 1, "picked up": 1, "picks up": 1,
"to star in": 2, "nabs": 1, "snags": 1, "in the works": 3, "lands at": 2, "sales": 1, "joins": 1, 
"to join": 2, "buys": 2, "to direct": 3, "to produce": 3, "casts": 2, "to play": 2, "debut": 1, 
"to make": 3, "acquire": 2, "development": 3, "circles": 2, "circling": 2, "sequel": -3, "trailer": -3, 
"dies": -3, "box office": -3, "film review": -3, "clip": -1, "remembers": -1, "release": -1, "award": -2,
"nominations": -3, "poll": -3, "$": -2, "oscars": -3, "rules": -1, "release": -1, "remember": -2, 
"premiere": -2, "spinoff": -3, "reboot": -3, "studio": -2, "sales": -1}



def nameExtraction(text, keyPhrase):
	'''Extract name roles from the article content.'''

	regEx = '([.][a-zA-Z0-9, ]*|[a-zA-Z0-9, ]*)' + keyPhrase + '(?!ly)(.*?)[.]'
	m = re.search(regEx, text)

	fullName = ''

	if m:
		found = m.group()
		subs = (found)
		print(subs)
		role = re.search('[A-Z][a-z]*[ ]([A-Z][a-z]*[ ]*)+', subs)
		#print(role.group())
		name = HumanName(role.group())
		fullName = name.first + " " + name.last
		print(fullName)

	return fullName


def scraper(url):
	'''Scrapes a full page'''

	movies = []

	#scrapes the full page
	html_page = urllib2.urlopen(url)
	soup = BeautifulSoup(html_page)


	#scrapes all links on the home page that are film related
	links = []
	for link in soup.findAll('a', attrs={'href': re.compile("^http://variety.com/[a-zA-Z0-9_/]*film")}):
	    #print (link.get('href'))
	    if (link.get('href') in links):
	    	continue
	    else:
	    	links.append(link.get('href'))


	movieTitle = []
	tagsHeader = []

	#scrapes all the content from the links
	for link in links:
		movie = {}

		#scrapes the article
		link_page = urllib2.urlopen(link)
		articleHTML = BeautifulSoup(link_page)

		#gets the title of the article
		tags = articleHTML.findAll('h1')
		tagsStr = str(tags[0])

		#gets the meta description of the article
		meta = articleHTML.find("meta", {"class":"swiftype", "data-type":"text"})

		#gets the article content from the meta description
		description = ''
		if meta:
			description = meta['content']


		#filters out relevant headlines based on keywords
		headerValue = 0;

		for key in headlineFilter.keys():
			if key in tagsStr.lower():
				headerValue = headerValue + headlineFilter[key]
		
		if(headerValue > 0):

			#finds name of roles
			movie["director"] = nameExtraction(description, "direct")
			movie["producer"] = nameExtraction(description, "produce")
			movie["actor"] = nameExtraction(description, "star")


			tagsHeader.append(tagsStr.lower())
			start = tagsStr.find('&#8216;') + 7
			end = tagsStr.find('&#8217', start)
			if("-" == tagsStr[end+7] 
				or "director" == tagsStr[end+8:end+16].lower()
				or "producer" == tagsStr[end+8:end+16].lower()
				or "star" == tagsStr[end+8:end+12].lower()):
				temp = tagsStr[end + 8:]
				start = temp.find('&#8216;') + 7
				end = temp.find('&#8217', start)
				
				if("</h1" in temp[start:end]):
					start = 4
					end = temp.find("</h1", start)
				if (temp[start:end] in movieTitle):
					continue
				movie["title"] = temp[start:end]
				continue

			if("</h1" in tagsStr[start:end]):
				start = 4
				end = tagsStr.find("</h1", start)
			if (tagsStr[start:end] in movieTitle):
				continue

			movie["title"] = tagsStr[start:end]

			movies.append(movie)

	return movies


def excel_writer(movies):

	workbook = xlsxwriter.Workbook('Movies.xlsx')
	worksheet = workbook.add_worksheet()

	worksheet.set_column(0, 0, 50)

	worksheet.write('A1', 'Title')
	worksheet.write('B1', 'Actor')
	worksheet.write('C1', 'Director')
	worksheet.write('D1', 'Producer')
	worksheet.write('E1', 'Plot')
	worksheet.write('F1', 'IMDB Rating')

	for movie in movies:

		#getting more info from the omdb API
		title = movie["title"]
		split = title.split()
		movieString = split[0]
		for i in range(1,len(split)):
			movieString+= "+" + split[i] 

		movieRequest = "http://www.omdbapi.com/?t=" + movieString

		r = requests.get(movieRequest)
		json = r.json()

		if 'imdbRating' in json.keys():
			imdbRating = json['imdbRating']
		else:
			imdbRating = 'Not found'

		if 'Plot' in json.keys():
			plot = json['Plot']
		else:
			plot = 'Not found'


		#excel writer
		worksheet.write_string(movies.index(movie)+1, 0,title)
		worksheet.write_string(movies.index(movie)+1, 1,movie["actor"])
		worksheet.write_string(movies.index(movie)+1, 2,movie["director"])
		worksheet.write_string(movies.index(movie)+1, 3,movie["producer"])
		worksheet.write_string(movies.index(movie)+1, 4,plot)
		worksheet.write_string(movies.index(movie)+1, 5,imdbRating)

	workbook.close()



def main():

	movies = []


	for pageNum in range(1,2):
		url = "http://variety.com/v/film/page/" + str(pageNum) + "/"
		movie = scraper(url)
		for m in movie:
			movies.append(m)


	excel_writer(movies)



main()
