import xml.etree.ElementTree as et
import requests
import csv


def loadRss():

    url='https://timesofindia.indiatimes.com/rssfeedstopstories.cms'

    #checking response
    response= requests.get(url)

    with open('xmlData.xml', 'wb') as file:
        file.write(response.content)

def parsingXml(xmlFile):

 #creatring a tree object
 tree= et.parse(xmlFile)

 #getting the root object from the tree object
 root= tree.getroot()

 #iterating to every element of the
 #declaring a new List
 NewsItems=[]
 for item in root.findall('./channel/item'):#declaration to get to every item tag under channel tag

    #declaring a news dictionary
    news= {}
    for child in item:

        # special checking for namespace object content:media
        if child.tag == '{http://search.yahoo.com/mrss/}content':
            news['media'] = child.attrib['url']
        else:
            try:
             news[child.tag] = child.text.encode('utf8')
            except:
                news[child.tag]= '---'

    NewsItems.append(news)

 return NewsItems

def saveToCsv(newsItems, fileName):

    fields= ['guid', 'title', 'pubDate', 'description', 'link', 'media']

    with open(fileName, 'r+') as csvFile:
     writer= csv.DictWriter(csvFile, fields)

     writer.writeheader()
     writer.writerows(newsItems)

def headlines():
 loadRss()
 newsItems= parsingXml('xmlData.xml')
 saveToCsv(newsItems, 'headlines.csv')
 return newsItems
