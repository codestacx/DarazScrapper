from bs4 import BeautifulSoup
import requests
import csv
import shutil
from requests_html import HTMLSession
session = HTMLSession()
import string
#  c1DXz4  items amount 

#  c1_t2i products items

#  c3e8SH > c5TXIP > cRjKsc  a >img 

#  c3e8SH > c5TXIP > c3KeDq > c16H9d > a = title

#  c3e8SH > c5TXIP > c3KeDq > c3gUW0 > span = price

# c3e8SH > c5TXIP > c3KeDq > c15YQ9  > c2JB4x c6Ntq9 > i = ratings

#  c3e8SH > c5TXIP > c3KeDq > c15YQ9 > span = location 
import random
import json

tracks = []
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
def download_image(image):
    url = image
    data = url.split('/')
    response = requests.get(url, stream=True)
    realname = data[-1]
    if realname in tracks:
        realname = id_generator()+realname
    tracks.append(realname)
    file = open("./images//iphone//{}.jpg".format(realname), 'wb')
    response.raw.decode_content = True
    shutil.copyfileobj(response.raw, file)
    del response


def scraper(url):
    data = requests.get(url)
    soup = BeautifulSoup(data.content,'html5lib')
    data = (soup.find_all('script', type='application/ld+json'))
    #print(data[1].text)
    data = json.loads(data[1].text)

    offers = (data['itemListElement'])
    #print(offers)
    products = []
    for offer in offers:
        product ={}
        for key,value in offer.items():
            if key == 'offers':
                for k,v in value.items():
                    product[k] = v
            else:
                product[key] = value
        products.append(product)
    print('total products fetched so far '+ str(len(products)) )
    writetocsv(products,'daraz_iphone.csv')


def writetocsv(products,filename):
    with open(filename, 'w') as f: 
        header=['priceCurrency','@type','price','availability','image','name','url','']
        w = csv.DictWriter(f,header) 
        w.writeheader() 
        for product in products:
            image = product['image']
            download_image(image) 
            w.writerow(product)

    

url = "https://www.daraz.com.bd/";
#scraper(url)

data = requests.get(url).text;
soup = BeautifulSoup(data.content,'ht')
list = soup.findAll("li",{"class":"menu-item"})
print(list)
#result = soup.findAll("a", {"class":"category"})
    
#print (result)

#print('daraz scrapped successfully')