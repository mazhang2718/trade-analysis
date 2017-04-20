from BeautifulSoup import BeautifulSoup
#from bs4 import BeautifulSoup
import urllib2
import re
from datetime import datetime
import xlsxwriter
 
html_page = urllib2.urlopen("http://variety.com/v/film/page/5/")
soup = BeautifulSoup(html_page)

headlineFilter = {"starts": 1, "adds": 1, "moving forward": 2, "in talks": 1, "to board":2, "boards":2, "teams up":1, 
"teams with":1, "reteams up": 1, "reteams with": 1, "picked up": 1, "picks up": 1,
"to star in": 2, "nabs": 1, "snags": 1, "in the works": 3, "lands at": 2, "sales": 1, "joins": 1, 
"to join": 2, "buys": 2, "to direct": 3, "to produce": 3, "casts": 2, "to play": 2, "debut": 1, 
"to make": 3, "acquire": 2, "development": 3, "circles": 2, "circling": 2, "sequel": -3, "trailer": -3, 
"dies": -3, "box office": -3, "film review": -3, "clip": -1, "remembers": -1, "release": -1, "award": -2,
"nominations": -3, "poll": -3, "$": -2, "oscars": -3, "rules": -1, "release": -1, "remember": -2, 
"premiere": -2, "spinoff": -3, "reboot": -3, "studio": -2, "sales": -1}



links = []

for link in soup.findAll('a', attrs={'href': re.compile("^http://variety.com/[a-zA-Z0-9_/]*film")}):
    #print (link.get('href'))
    if (link.get('href') in links):
    	continue
    else:
    	links.append(link.get('href'))


movieTitle = []
tagsHeader = []

#print(headlineFilter)

for link in links:
#link = links[0]
	#print(link)
	html_page1 = urllib2.urlopen(link)
	soup1 = BeautifulSoup(html_page1)
	tags = soup1.findAll('h1')
	
	tagsStr = str(tags[0])
	headerValue = 0;

	#print(tagsStr)
	for key in headlineFilter.keys():
		if key in tagsStr.lower():
			#print("it got here")
			#print(key)
			#print(tagsStr)
			headerValue = headerValue + headlineFilter[key]
	

	if(headerValue > 0):
		tagsHeader.append(tagsStr.lower())
		start = tagsStr.find('&#8216;') + 7
		end = tagsStr.find('&#8217', start)
		if("-" == tagsStr[end+7] 
			or "director" == tagsStr[end+8:end+16].lower()
			or "producer" == tagsStr[end+8:end+16]
			or "star" == tagsStr[end+8:end+12]):
			temp = tagsStr[end + 8:]
			start = temp.find('&#8216;') + 7
			end = temp.find('&#8217', start)
			
			if("</h1" in temp[start:end]):
				start = 4
				end = temp.find("</h1", start)
			if (temp[start:end] in movieTitle):
				continue
			movieTitle.append(temp[start:end])
			continue

		if("</h1" in tagsStr[start:end]):
			start = 4
			end = tagsStr.find("</h1", start)
		if (tagsStr[start:end] in movieTitle):
			continue

		movieTitle.append(tagsStr[start:end])
	#print(tags)
	#print(tagsStr[start:end])



workbook = xlsxwriter.Workbook('Expenses03.xlsx')
worksheet = workbook.add_worksheet()

print(movieTitle)
#print(len(tagsHeader))
#print(tagsHeader)

worksheet.set_column(0, 0, 50)

worksheet.write('A1', 'Title')
worksheet.write('B1', 'Stars')
worksheet.write('C1', 'Director')



for movie in movieTitle:
	worksheet.write_string(movieTitle.index(movie)+1, 0,movie)

workbook.close()

	#r = re.compile("*")
	#newlist = filter(r.match, tags)
	#print(str(tags[0]))
	#tags = soup1.findAll(re.compile("[a-z]"))

#for text in soup1.findAll('h1'):
	#print(tags)
    #links.append(link.get('href'))

#print(links)

