import requests
from bs4 import BeautifulSoup

result = requests.get("https://news.google.com/?hl=en-IN&gl=IN&ceid=IN:en")
print(result.status_code)
src = result.content
soup = BeautifulSoup(src,'lxml')
links=soup.find_all("h3")

urls = []
i=1
for h3_tags in links:
    a_tag = h3_tags.find('a')
    urls.append(a_tag)
    print('%d) %s'%(i,a_tag.text))
    print("\n")
    i=i+1

