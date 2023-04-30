# import requests
# from bs4 import BeautifulSoup
# import csv
# from itertools import zip_longest

# product_titles = []
# product_images = []
# price_current = []
# price_line = []


# use requests to fetch the URL
# result = requests.get("https://www.citymall.ma/search.php?mode=search&page=1&keep_https=yes")
# src = result.content

# create soup object to parse content
# soup = BeautifulSoup(src, "lxml")

# Find all <a> elements with class "product-title"
# titles = soup.find_all("a", class_="product-title")
# price = soup.find_all("span", class_="price-value")
# div = soup.find('div', attrs={'id': 'center-main'})



# Iterate over each element and retrieve the text
# for omg in img:
#     print(omg['href'])




variable = ["imagin","dalida","donor"]

for i in range(2):
    print(variable[i])










# div = soup.find('div', attrs={'id': 'center-main'})
# title = div.find('h1').text
# prix = soup.find_all('span', attrs={'class': 'currency'}) 
# descr = soup.find('div', attrs={'class': 'descr'}).text 
# src_image = soup.find('img', attrs={'id': 'product_thumbnail'})
# Links =[]

# for s in src:
#     Links.append(s['href'])


# for i in range(len(title)):
#     product_titles.append(title[i].text)
#     product_images.append(src_image[i].find('a')['href'])
#     price_current.append(prix[i].text)
#     print(price_current)
   





# print(product_titles)


# file_List = [product_titles, product_images, price_current, price_line]
# with open("/Users/naini/Documents/scrip.csv", "w") as myfile:
#     wr = csv.writer(myfile)
#     wr.writerow(["title", "image", "price", "price-line"])
#     wr.writerows(file_List)





