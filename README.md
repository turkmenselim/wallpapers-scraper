# Wallpapers Scraper
Firstly, this project just made for educational reasons. It has no commercial purpose.

---
## Requirements
- beautifulsoup4==4.11.1
- requests==2.27.1
---
## Meaning of codes

Firstly we should run category_scraper.py because of scraping category links from website. <br />
After that we can run image_scraper.py file to downlaod images with image links. 

---

# Folder path for saving images
For saving images we should write a folder path in image_scraper.py file.
```
# image_scraper.py file

os.chdir(os.path.join(os.getcwd(),r'<folder_path_for_saving_images>'))
```
Then we can run image_scraper.py file.

![resim](https://user-images.githubusercontent.com/33834961/201997061-0ae7fc26-8482-4650-9cb9-96520c30f03f.png)
