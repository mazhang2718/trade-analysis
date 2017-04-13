from BeautifulSoup import BeautifulSoup
#from bs4 import BeautifulSoup
import urllib2
import re
from datetime import datetime
import xlsxwriter
 
html_page = urllib2.urlopen("http://variety.com/v/film/")
soup = BeautifulSoup(html_page)


links = []

for link in soup.findAll('a', attrs={'href': re.compile("^http://variety.com/[a-zA-Z0-9_/]*film")}):
    #print (link.get('href'))
    if (link.get('href') in links):
    	continue
    else:
    	links.append(link.get('href'))


movieTitle = []

for link in links:
#link = links[0]
	#print(link)
	html_page1 = urllib2.urlopen(link)
	soup1 = BeautifulSoup(html_page1)
	tags = soup1.findAll('h1')
	
	tagsStr = str(tags[0])

	start = tagsStr.find('&#8216;') + 7
	end = tagsStr.find('&#8217', start)

	if ("</h1" in tagsStr[start:end] or tagsStr[start:end] in movieTitle):
			continue

	movieTitle.append(tagsStr[start:end])
	#print(tags)
	#print(tagsStr[start:end])



workbook = xlsxwriter.Workbook('Expenses03.xlsx')
worksheet = workbook.add_worksheet()

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

