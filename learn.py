import bs4
import requests
from bs4 import BeautifulSoup
link  ="https://www.cricbuzz.com/cricket-match/live-scores"
r = requests.get(link)
content = r.content
soup = BeautifulSoup(content,'html.parser')
team = soup.select('cb-col-100 cb-col cb-schdl cb-billing-plans-text')
#print(type(team))
#print(soup.title)
#print(team)


#title =soup.title
#print(type(title.string))

#para =soup.find_all('p')

#print(type(anchor))
#print(para)
#print("PARAGRAPH LIST")
#for i in para:
   # print(i.getText)

#div =soup.find_all('div',class_='cb-mtch-lst cb-col cb-col-100 cb-tms-itm')
#print("CONTAINER LIST")
#for i in div:
    #print(i.getText)

title =(soup.find('h1',attrs={'class':"cb-nav-hdr cb-font-24 line-ht30"}))
print(title.text)
print('\n')

matchname = soup.find_all('h2',attrs={'class':'cb-lv-grn-strip text-bold cb-lv-scr-mtch-hdr'})
mathtitle = soup.find_all('div',attrs={'class':'cb-col-100 cb-col cb-schdl cb-billing-plans-text'})
scores = soup.find_all('a',attrs={'class':'cb-lv-scrs-well cb-lv-scrs-well-live'})
for i in matchname:
    for j in mathtitle:
        for k in scores:
          print(i.text)
          print(j.text)
          print(k.text)
          print('\n')







