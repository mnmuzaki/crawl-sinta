import requests
from bs4 import BeautifulSoup
count= 0

#substring untuk max page


#crawl data
page = 1
draft = "https://sinta.kemdikbud.go.id/affiliations/profile/2099?page="+str(page)+"&view=scopus"
url = draft
#membuat request
r = requests.get(url)

request = r.content

soup = BeautifulSoup(request, 'html.parser')

#extract element
title = soup.findAll('div',attrs={'class':'ar-title'})
quartile = soup.findAll('a',attrs={'class':'ar-quartile'})
pub = soup.findAll('a',attrs={'class':'ar-pub'})
year = soup.findAll('a',attrs={'class':'ar-year'})
cited = soup.findAll('a',attrs={'class':'ar-cited'})
paging = soup.find('div',attrs={'class':'text-center pagination-text'})
print(paging)
for x in range(0,len(title)):
    count += 1
    print("{0}. {1}. {2}. {3}. {4}".format(count, title[x].text.strip() , quartile[x].text.strip(), pub[x].text.strip(), year[x].text.strip(), cited[x].text.strip()))