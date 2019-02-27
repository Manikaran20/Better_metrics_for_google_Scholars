import bs4
import urllib
from bs4 import BeautifulSoup as soup 
from selenium import webdriver

import re

title_list = []
Citations =[]
coAuths = []
n_citations = []


class Scraper():

	def __init__(self, url, maxP):

		self.url= url

		self.maxP = maxP

	def f(self):

		for i in range(0,1000,100):

			if (int(self.maxP.encode('utf-8'))<=i):
				pageSize = i
				break

		for j in range(0,pageSize, 100):

			S_url=self.url + "&cstart=" + str(j) +"&pagesize=100"

			

			my_url = urllib.urlopen(S_url)

			page_html = my_url.read()

			my_url.close()

			page_soup = soup(page_html, "html.parser")

			aTag = page_soup.findAll('td', {'class': 'gsc_rsb_std'})

			Titles = page_soup.findAll('td', {'class': 'gsc_a_t'})

			Citations_soup = page_soup.findAll('td', {'class': 'gsc_a_c'})

			Years = page_soup.findAll('td', {'class': 'gsc_a_y'})

			info_page = page_soup.findAll('a', {'class' : 'gsc_a_at'})

			driver =  webdriver.Firefox()

			for author in info_page:

				Author_names_link = author["data-href"]

				user=Author_names_link[53:65]


				n_input=Author_names_link[-12:]

				n_author_url="https://scholar.google.com.au/citations?user="+user+"&hl=en#d=gs_md_cita-d&u=%2Fcitations%3Fview_op%3Dview_citation%26hl%3Den%26user%3D"+user+"%26citation_for_view%3D"+user+"%3A"+n_input+"%26tzom%3D-330"

				driver.implicitly_wait(30)

				driver.get(n_author_url)

				title= driver.find_elements_by_xpath('//div[@class="gsc_vcd_value"]')

				page_element = title[0].text

				coAuths.append(len(page_element.split(',')))


			for title in Titles:
				Title = title.a.text
				title_list.append(Title)
			
			for c in Citations_soup:
				p= c.text.encode('utf-8')
				q= re.findall('[0-9]+',p)
				Citations.append(q)

		
		n_papers= 0

		for element in range(len(title_list)):

			n_papers +=1/coAuths[element]

			try:
				n_citations.append(int(Citations[element][0])/coAuths[element])
			except:
				n_citations.append(0)
			print (n_citations)

		print (sum(coAuths))

		sum_citations= 0

		for k in Citations:
			try:
				sum_citations+= int(k[0])
				print ('a',sum_citations)
			except:
				continue

			print (sum(coAuths))
		T_citations = sum_citations/sum(coAuths)
		print (T_citations)
		print (n_papers)
		print (n_citations)


		return (T_citations, n_papers, n_citations)
		
