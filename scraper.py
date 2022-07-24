import requests
from bs4 import BeautifulSoup


#this base url is what each has in common in the href
base_url = 'https://www.jumia.com.ng'

#browser agent settings
headers = {
		"X-RapidAPI-Key": "6b28618dc7mshaab549a1ca56647p1f7cafjsnddabc557ad37",
		"X-RapidAPI-Host": "jumia-service.p.rapidapi.com"
	}


#container for the extract links
product_links=[]
#if you want the whole jumia phones increase the page range below max=50
for page in range(1,2):
#request from jumia phone page1
    url = f'https://www.jumia.com.ng/mobile-phones/?page={page}#catalog-listing'
    response = requests.request("GET", url, headers=headers)
    soup = BeautifulSoup(response.content, "lxml")
    #scrapping the reccurent div class
    product_list=soup.find_all('div',class_='itm col')

    #the code below will loop through the link and merge the base url with each product
    for item in product_list:
        for link in item.find_all('a', href=True):
            product_links.append(base_url+ link['href'])

pack=[]
user=input('Enter the phone brand: ').lower()
for link in product_links:

    r=requests.get(link,headers=headers)
    soup= BeautifulSoup(r.content, 'lxml')
    #colecting informations

    brand_check=list(soup.find('h1', class_='-fs20 -pts -pbxs').text.strip().split())[0].lower()
    brand=soup.find('h1', class_='-fs20 -pts -pbxs').text.strip()
    price= soup.find('span',class_='-b -ltr -tal -fs24').text
    review= soup.find('div',class_='stars _s _al').text
    #store data
    store={
        'brand':brand,
        'review':review,
        'price':price,
        'link':link
    }
   
    if user==brand_check:
         pack.append(store)

print(pack)

