import requests
from bs4 import BeautifulSoup

######################################### MEMASUKKAN SESSION ################################### 
#import requests

cookies = {
    '_ga_DDV4DPGV0H': 'GS1.1.1698995664.2.0.1698995669.0.0.0',
    '_ga_2BMHYQ15QC': 'GS1.1.1704709608.5.1.1704710422.0.0.0',
    '_ga_6NXX5DTK0E': 'GS1.1.1705388744.6.1.1705388914.0.0.0',
    '_ga': 'GA1.1.496501778.1692680010',
    'ci_session': '975lbaovtvo5ghvorokk3kte7u8eau3d',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    # 'Cookie': '_ga_DDV4DPGV0H=GS1.1.1698995664.2.0.1698995669.0.0.0; _ga_2BMHYQ15QC=GS1.1.1704709608.5.1.1704710422.0.0.0; _ga_6NXX5DTK0E=GS1.1.1705388744.6.1.1705388914.0.0.0; _ga=GA1.1.496501778.1692680010; ci_session=975lbaovtvo5ghvorokk3kte7u8eau3d',
    'Referer': 'https://sinta.kemdikbud.go.id/logins',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

#response = requests.get('https://sinta.kemdikbud.go.id/', cookies=cookies, headers=headers)
################################ AKHIR MEMASUKKAN SESIONS ##################################
#get max page


#crawl data https://sinta.kemdikbud.go.id
#page = 0
stop = 13
count= 0
for page in range(1,20):
    #page += 1
    draft = "https://sinta.kemdikbud.go.id/affiliations/profile/2099?page="+str(page)+"&view=scopus"
 
    url = draft

    #membuat request
    r = requests.get(url, cookies=cookies, headers=headers)

    request = r.content

    soup = BeautifulSoup(request, 'html.parser')

    #extract element
    title = soup.findAll('div',attrs={'class':'ar-title'})
    quartile = soup.findAll('a',attrs={'class':'ar-quartile'})
    pub = soup.findAll('a',attrs={'class':'ar-pub'})
    year = soup.findAll('a',attrs={'class':'ar-year'})
    cited = soup.findAll('a',attrs={'class':'ar-cited'})
    #paging = soup.find('div',attrs={'class':'text-center pagination-text'})
    #print(paging)
    #print(soup.get_text("1 of 12"))
    for x in range(0,len(title)):
        count += 1
        print("{0}. {1}. {2}. {3}. {4}. {5} ".format(count, title[x].text.strip() , quartile[x].text.strip(), pub[x].text.strip(), year[x].text.strip(), cited[x].text.strip()))

    #stop = len(title)
    