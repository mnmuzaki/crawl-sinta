import requests
import re
from bs4 import BeautifulSoup

######################################### MEMASUKKAN SESSION ################################### 
# Mengkonversi curl pada tautan https://curlconverter.com/
cookies = {
    '_ga_DDV4DPGV0H': 'GS1.1.1698995664.2.0.1698995669.0.0.0',
    '_ga_2BMHYQ15QC': 'GS1.1.1704709608.5.1.1704710422.0.0.0',
    '_ga_6NXX5DTK0E': 'GS1.1.1705388744.6.1.1705388914.0.0.0',
    '_ga': 'GA1.1.496501778.1692680010',
    'ci_session': '9qfp86ahtotb97c3e6ip7etq3pakb1oe',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    # 'Cookie': '_ga_DDV4DPGV0H=GS1.1.1698995664.2.0.1698995669.0.0.0; _ga_2BMHYQ15QC=GS1.1.1704709608.5.1.1704710422.0.0.0; _ga_6NXX5DTK0E=GS1.1.1705388744.6.1.1705388914.0.0.0; _ga=GA1.1.496501778.1692680010; ci_session=9qfp86ahtotb97c3e6ip7etq3pakb1oe',
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

#response = requests.get('https://sinta.kemdikbud.go.id/', cookies=cookies, headers=headers)
################################ AKHIR MEMASUKKAN SESIONS ##################################
#get max page
list_prodi = ['PGSD',
              'PENJAS',
              'PGPAUD',
              'PPG',
              'MANAJEMEN',
              'Pendidikan Matematika',
              'Bimbingan Dan Konseling',
              'TI',
              'SI',
              'MKO',
              'AKUNTANSI',
              'BIOLOGI',
              'PBSI',
              'TEKNIK MESIN',
              'Pendidikan Ekonomi',
              'Peternakan',
              'Pendidikan Bahasa Inggris',
              'Teknik Elektronika',
              'Pendidikan Sejarah',
              'Keperawatan',
              'Keperawatan',
              'Teknik Industri',
              'Pendidikan Ekonomi',
              'Kebidanan'
              ]
list_link = ['21781CCB-9B5B-4953-9D14-FEA1A4788FA2',
             'AEF1ADDD-AAC6-4FB7-A5B3-26032FC01688',
             '3BB2CB06-7698-4F0D-99E6-BBF5807217A8',
             '18C9E582-04C4-4051-B7E1-D31943F2E633',
             '5B3270BA-255C-492F-A156-81DFF9D4A460',
             '647B57EE-C37A-4A53-93A8-6C0EA4C7D24E',
             'FA851842-1C7F-455A-91F1-4BFAD68BB234',
             'D1FDE601-8912-4AEC-816D-841B2D440C4F',
             'F05857A7-6E00-4BA4-BB91-425E6D7003FD',
             '6A36BB6C-4B34-4382-8C5B-54734D4C31E8',
             'EAB2C355-5454-453F-ABEF-F9C6A84C239E',
             '9E887C02-357F-4BA4-888B-55AD856A3E19',
             'AEB68FBC-18AB-4077-B26D-0A26F9B45D0B',
             '8598BBD9-B45B-4652-A69A-16CF05595474',
             '71B5398A-5C2D-4851-A776-AF7A5EBCC3B9',
             '17882E48-DBFA-452C-91DF-ACD56ADEDB54',
             '0EBE510D-986A-46A5-908F-EE76CE72C418',
             '3075D776-29B3-418E-B8C6-D1075B40CE38',
             '70B4C6A0-DB86-4EA7-A2B4-57B2472A95A3',
             '4BDF6F7E-F0AB-4D95-8325-3C3AB84E38EA',
             'A0A5D7C6-F2D1-4B11-927D-6CA1B0820E91',
             'CD1E0951-90EA-4A86-A938-31384B4F7A52',
             'F67DBD4F-929D-4C92-AFFC-4F409545C3B9',
             '3B445DBE-9145-48AB-9C69-F82A608920DF'
             ]
# OPEN FILE #
file_hasil = open("hasil/scopus-prodi.txt", "w")
# AKHIR OPEN FILE #

#crawl data https://sinta.kemdikbud.go.id
#page = 0

#print(len(list_prodi))
#print(len(list_link))
list_title = []

for z in range(0,len(list_prodi)):
    list_title.clear()
    stop = 11
    count= 0
    file_hasil.write(list_prodi[z]+"\n"+"============================="+"\n") 
    for page in range(1,5):
        if page > stop :
                break
        #page += 1
        draft = "https://sinta.kemdikbud.go.id/departments/profile/2099/F5D8DB12-BB00-4849-A75E-126843A7DB35/"+str(list_link[z])+"?page="+str(page)+"&view=scopus"
    
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

        paging = soup.findAll('small')
        #print(paging)
        #print(soup.get_text("1 of 12"))
        #list_title = [title[0].text.strip()]
        ######################### Mencari panjang page
        #print(paging[1].text.strip())
        text = str(paging[1].text.strip())
        cocok = re.search(r' of\s+(.*?)\s+| Total Records', text)
        print(cocok.group(1))
        if cocok != None :
            s = cocok.group(1)
            t = int(s)
        else :
            t = 0;
        print(t)
        print(list_prodi[z])
        
        for x in range(0,len(title)):
            count += 1
            if title[x].text.strip() in list_title :
                 break
            else:
                list_title.append(title[x].text.strip())
                #if title[x].text.strip() not in list_title:
                #if list_title[count-1] == list_title[0] and count > 1:
                print("{0}. {1}. {2}. {3}. {4}. {5} ".format(count, title[x].text.strip() , quartile[x].text.strip(), pub[x].text.strip(), year[x].text.strip(), cited[x].text.strip()))
                teks = "{0}; {1}; {2}; {3}; {4}; {5} \n".format(count, title[x].text.strip() , quartile[x].text.strip(), pub[x].text.strip(), year[x].text.strip(), cited[x].text.strip())
                file_hasil.write(teks) 
                #stop = len(title)
        stop = t
  #  print(list_title)
    