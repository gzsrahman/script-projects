# Let's import some fun tools
import bs4 as bs
import urllib.request
import re
import pandas as pd 
from time import sleep
import os

#######################################################################################
# PART 1: TEXT SCRAPING
#######################################################################################

# Lets scrape the info from the transcripts of Anderson Cooper 360 on CNN

# Getting our source
# I encourage you to look at the page HTML before running the code
source = urllib.request.urlopen("https://transcripts.cnn.com/show/acd").read()

# Let's make the HTML easier to read
soup = bs.BeautifulSoup(source, features="lxml")

# We're gonna create an id for the urls so we can pull all of the urls out
# for processing
urls_css = ".cnnSectBulletItems a"
urls = soup.select(urls_css)
extracted_urls = [url["href"] for url in urls]
full_urls = ["https://transcripts.cnn.com/" + url_suffix for url_suffix in extracted_urls]

# Let's just do the first 5; I'm assuming you don't want to download every single
# Andy Coop segment there's ever been (before you ask... yes, we're tight like that)
urls_to_scrape = full_urls[0:5]

# We're gonna store the transcript in texts and we're gonna loop through each
# url to get the information. We're using sleep(5) so there's a 5 second pause
# in between each loop. We don't want the website to think it's getting attacked
texts = []
for i in urls_to_scrape:
  sleep(5)
  source = urllib.request.urlopen(i).read()
  soup = bs.BeautifulSoup(source, features = "lxml")
  text_css = ".cnnBodyText"
  text = soup.select(text_css)
  texts.append(str([i.text for i in text]))

print("I'm assuming you don't want to print a huge chunk of text into your terminal.")
print("If you would, please uncomment the two lines below this print statement and")
print("run the code again.")
# for i in texts:
#   print(i)

#######################################################################################
# PART 2: IMAGE SCRAPING
#######################################################################################

# Let's scrape and download images of major world leaders listed on Wikipedia

# Getting the source and making it readable
source = urllib.request.urlopen("https://en.wikipedia.org/wiki/G20").read()
soup = bs.BeautifulSoup(source, features="lxml")

# Extracting the text from the leader profile section
urls_css = ".gallerytext a"
urls = soup.select(urls_css)

# Isolating text from html from extracted information
extracted_names = [url.text for url in urls]

# Housekeeping, extra text value in dataset
extracted_names.remove('[d]')

# Iterating through the loop using pattern to extract leader names
names = []
i = 1
while i < len(extracted_names):
  names.append(extracted_names[i])
  i += 3

# Getting all of the image urls by specifying where they are contained
imgurls_css = ".thumb img"
img_urls = soup.select(imgurls_css)
image_urls = [item["src"] for item in img_urls]

# For some reason, image_urls includes "//" at the beginning of every string
# So let's remove that
img_urls = []
for img in image_urls:
  img_urls.append('https://' + img[2:])

# Also for some reason, we have an extra image at the end, so let's take it out
img_urls.remove(img_urls[-1])

df = pd.DataFrame(columns=('face_name', 'face_url'))
df['face_name']=names
df['face_url']=img_urls

print("I'm assuming you don't want a file created without your permission, nor")
print("would you want a folder full of world leaders on your device. If I'm wrong")
print("feel free to uncomment the next 3 lines below this print statement to create")
print("a file with a list of world leader image urls")
print("Afterwards, type the wget statement into your terminal, adapting the paths")
print("to your desired specifications.")
# with open("imgs_to_download.txt", 'w') as f:
#   for i in df['face_url']:
#     f.write(str(i) + "\n")

# wget -i /content/imgs_to_download.txt -P /content/world_leaders/

