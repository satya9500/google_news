from bs4 import BeautifulSoup
import requests
result = requests.get("https://www.polygon.com/games")
src=result.content
soup=BeautifulSoup(src,'lxml')

game_index=soup.find_all('ul',{'class':'m-game--index__list'})

for li in game_index:
    li.find_all()
    print(li.text)
  
   
        


