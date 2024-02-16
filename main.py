import requests
from  bs4 import BeautifulSoup

url = "http://www.codewithharry.com"

r = requests.get(url)
htmlContent =  r.content
#print(htmlContent)

soup =  BeautifulSoup(htmlContent,  'html.parser')
#print(soup.prettify())


# Commaly used types of objects
#1. Tag
#2. NavigableString
#3 . BeautifulSoup
#4. Comment 


# markup =  "<p><! -- this is comment --></p>"
# soup2 = BeautifulSoup(markup)
# print(type(soup2.p.string))



# title =  soup.title    # title of html page 
# print(type(title.string))
# print(type(soup))
# print(type(title))




# Get all the paragraphs of the page

paras =  soup.find_all('p')
#print(paras)



# print(soup.find('p'))    #get first element
# print(soup.find('p')['class'])   # get classes of any element in the page


#find all the elemnts with class  

# #


# get the text from the tags/soup 

#print(soup.find('p').get_text())



# Get all the anchortags of the page

anchors =  soup.find_all('a')
all_links = set()
# get all the links on the page:
for link in anchors:
    if(link.get('href')  !=  '#'):
        linkText  =  "http://codewithharry.com" + link.get_text("href")
        all_links.add(link)
        #print(linkText)
     
    

#print(anchors)




#  .contents - A tag's children are available as a List
# .children - A tag's children are available as genrator
navbarSupportedContent =  soup.find(id ="imgpreview2")

# for elem in navbarSupportedContent.contents:
#     print(elem)


# for item in navbarSupportedContent.strings:
#     print(item)
# for item in navbarSupportedContent.stripped_strings:
#     print(item)


# for  item in navbarSupportedContent.parents:
#     print(item)
#     print(item.name)


print(navbarSupportedContent.next_sibling.next_sibling)


elem =  soup.select('.model-footer')
print(elem)

















