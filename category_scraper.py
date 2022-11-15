import requests
import bs4

url = "https://wallpapers.com/music"

r = requests.get(url)

soup = bs4.BeautifulSoup(r.text,"html.parser")

ctg_tags = soup.find_all("a", class_="caption stretched-link")
link_list= list()
number = 0
for links in ctg_tags:
    link = links["href"]
    link_list.append(link)
    number +=1
print("number of category: "+str(number))
print(link_list)

