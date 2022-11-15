import bs4
import requests
import os
from category_scraper import link_list

os.chdir(os.path.join(os.getcwd(),r'C:\Users\charl\Desktop\OLD\wallpaperscom\Görseller'))
img_count=1
for i in link_list:
    r = requests.get(i)
    soup = bs4.BeautifulSoup(r.text,"html.parser")
    img_tags = soup.find_all("img", class_="lozad")
    try:
        for image in img_tags:
            name = image["alt"]
            src = image["data-src"]
            link = "https://wallpapers.com"+src

            img_download = requests.get(link).content
            with open(name+".jpg","wb") as handler:
                handler.write(img_download)
            print(name+ " is downloaded. Total Image Count: "+str(img_count))
            img_count += 1
    except Exception as e:
        print(e)


