import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest
import os

PRODUCTS=[]

src = []

# use requests to fetch the url

for i in range(497,517,1):
    try:
        result = requests.get("https://www.citymall.ma/search.php?mode=search&page="+str(i))
        print("https://www.citymall.ma/search.php?mode=search&page="+str(i))
        src = result.content
        soup = BeautifulSoup(src, "lxml")
    except requests.exceptions.MissingSchema:
        print("Invalid URL page number"+str(i))
        continue
    

    src = soup.find_all("a", {"class": "product-title"})
    Links =[]
    for s in src:
        Links.append(s['href'])

    #fetch data 

    for src in Links : 
        product=[]
        try:
            result = requests.get(src)
        except requests.exceptions.MissingSchema:
            print("Invalid URL provided. Please include a valid protocol in the URL.")
            continue
        src = result.content
        soup = BeautifulSoup(src, "lxml")
        div = soup.find('div', attrs={'id': 'center-main'})
        title = div.find('h1').text
        prix = soup.find('span', attrs={'id': 'product_price'}).text 
        descr = soup.find('div', attrs={'class': 'descr'}).text 
        src_image = soup.find('img', attrs={'id': 'product_thumbnail'})
        cate= soup.find_all('a', attrs={'class': 'bread-crumb'})
        category=""
        for c in cate:
            if c.text != 'Acceuil':
                category+=str(c.text)
                category+=" // "

        try:
            image_url = src_image['src']
            # path fin ghat7at limage
            folder_path = "./product_images"  
            response = requests.get(image_url)
            file_name = image_url.split("/")[-1]
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, "wb") as file:
                file.write(response.content)
        except FileNotFoundError:
            print('Le fichier spécifié est introuvable in page :'+str(i)+' Tilte :'+title)
            continue

        product=[title,prix,descr,file_name,category]
        PRODUCTS.append(product)
    try:
        if i == 1 : 
            with open('data.csv', 'w', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(["Title", "Prix", "Description", "Image","Categorie"])
                writer.writerows(PRODUCTS)
        else:
            with open('data.csv', 'a', encoding='utf-8') as file:
                writer = csv.writer(file)
                for row in PRODUCTS:
                    writer.writerow(row)
    except PermissionError:
        # Handle the PermissionError
        print("Problem f CSV.")


    PRODUCTS=[]
    print('page '+str(i)+' SALAT')


    
    



