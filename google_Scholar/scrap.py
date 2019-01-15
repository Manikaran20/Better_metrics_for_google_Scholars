import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup 

my_url = 'https://scholar.google.com.au/citations?user=m8dFEawAAAAJ&hl=en'
uClient = uReq(my_url) # opening a connection
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")

aTag = page_soup.findAll('td', {'class': 'gsc_rsb_std'})

Titles = page_soup.findAll('td', {'class': 'gsc_a_t'})

Citations = page_soup.findAll('td', {'class': 'gsc_a_c'})

Years = page_soup.findAll('td', {'class': 'gsc_a_y'})

for title in Titles:
	coAuth = title.findAll('div', {'class': 'gs_gray'})
	coAuths = coAuth[0].text
	Title = title.a.text
	print (coAuths)
	print (Title)

for citations in Citations:
	citation = citations.text
	print (citation)


for year in Years:
	Year= year.text

print (len(Years))
print (len(Citations))
print (coAuths)
total= aTag[0].text
since2014= aTag[1].text

