# -*- coding: utf-8 -*-
import os, sys

#from BeautifulSoup import BeautifulSoup
#from bs4 import BeautifulSoup
#import urllib2
import re
from datetime import datetime
from nameparser import HumanName
#import xlsxwriter


#s = u'Ambi Pictures has wrapped production in Argentina on “Beyond the Sun,” with Pope Francis appearing as himself, and will launch international sales at the Cannes Film Festival. Ambi announced the project last year, touting it as the first time that a pope has ever appeared in a feature film. Written and directed by Graciela Rodriguez, “Beyond the Sun” stars child actors Aiden Cumming-Teicher, Cory Gruter-Andrew, Emma Duke, Kyle Breitkopf, and Sebastiάn Alexander Chou. The pope asked the filmmakers to develop a movie for children that communicates Jesus’ message and said he was willing to participate in the movie to support charity as all profits from “Beyond the Sun” will be donated to two Argentinian charities — El Almendro and Los Hogares de Cristo, which provide aid to at-risk children and young adults in need. Ambi co-founders Andrea Iervolino and Lady Monika Bacardi produced the film and were advised by Monsignor Eduardo Garcia. The co-producers are Graciela Rodriguez and Gabriel Leybu. The movie is financed by AMBI in association with Raven Capital Management and Paradox Studios. Ambi will present “Beyond the Sun” in Cannes through its Los Angeles-based international sales division, Ambi Distribution. The festival launches May 17.'
#s = u'Fisher Stevens, who directed “Bright Lights: Starring Carrie Fisher and Debbie Reynolds,” has signed on to direct the independent drama “Palmer” for Route One Entertainment. Shooting will start by the end of June.'
#s = u'Chris Pine and Michelle Williams are in negotiations to co-star in the Mark Gordon Company’s spy thriller “All the Old Knives,” sources tell Variety. “Theory of Everything” helmer James Marsh is also in negotiations to direct, the sources add.'
s = u'Paramount has moved the release of “Transformers: The Last Knight” forward by two days to June 21, which is a Wednesday. It remains the studio’s top prospect for 2017. The four previous “Transformers” installments have grossed $3.77 billion worldwide, including $1 billion for the most recent “Transformers: Age of Extinction” in 2014. It’s the only new wide release for the the June 23-25 weekend. Paramount offered a well-received 15-minute sneak peak at Mark Wahlberg’s “Transformers: The Last Knight” on March 28 at CinemaCon. Michael Bay, who is directing his final “Transformers,”  touted the film as being the first to be shot entirely in Imax 3D.'
m = re.search('([.][a-zA-Z0-9, ]*|[a-zA-Z0-9, ]*)direct(?!ly)(.*?)([A-Z][a-z]*[ ][A-Z][a-z]*|[.]|[“])', s)

#start = m.find('AAA'

if m:
    found = m.group(1)
    subs = str(found)
    director = re.search('[A-Z][a-z]*[ ]([A-Z][a-z]*[ ]*)+', subs)
    name = HumanName(str(director.group()))
    print(name.first, name.last)
    #print(found)


#----------below is for finding producer--------------------
s1 = u'Bailee Madison will star in the movie adaptation of Rachel Bateman’s coming-of-age novel “Someone Else’s Summer.” Producer Beth Grossbard landed the option and will produce via her eponymous company. The novel will be published this month by Running Press Kids/Hachette Book Group and is going to auction for international rights. “Someone Else’s Summer” follows a young woman whose life gets turned upside down after her sister dies on the night of her high school graduation. Madison’s character sets out to honor her sister by fulfilling everything on her summer bucket, including a road trip with her sister’s best friend/the boy next door, which takes them from their sleepy Iowa town to the shores of the Atlantic.'
m1 = re.search('([.][a-zA-Z0-9, ]*|[a-zA-Z0-9, ]*)produce(?!ly)(.*?)([A-Z][a-z]*[ ][A-Z][a-z]*|[.]|[“])', s1)


if m1:
    found1 = m1.group(1)
    subs1 = str(found1)
    producer = re.search('[A-Z][a-z]*[ ]([A-Z][a-z]*[ ]*)+', subs1)
    name = HumanName(str(producer.group()))
    #name = HumanName(" Producer Beth Grossbard")
    print(name.first, name.last)
    #print(found1)



