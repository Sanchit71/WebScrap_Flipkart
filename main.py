import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

# List to store the data
Product_Name = []
Price = []
Description = []
Rating = []
Reviews = []

# Iterating the number of pages
for j in range(2, 34):
    # Link of the page
    url = "https://www.flipkart.com/search?q=laptop+under+50000+with+reviews&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&p%5B%5D=facets.rating%255B%255D%3D3%25E2%2598%2585%2B%2526%2Babove&page=" + \
        str(j)

    # Requesting the page
    r = requests.get(url)
    # print(r)

    # Extracting the data from the page
    soup = BeautifulSoup(r.text, "html5lib")
    box = soup.find("div", class_="_1YokD2 _3Mn1Gg")

    # Product Name
    p_names = box.find_all("div", class_="_4rR01T")
    for i in p_names:
        name = i.text
        Product_Name.append(name)
    # print(len(Product_Name))

    # Price of Product
    pri = box.find_all("div", class_="_30jeq3 _1_WHN1")
    for i in pri:
        name = i.string
        Price.append(name)
    # print(Price)

    # Description of Product
    des = box.find_all("div", class_="fMghEO")
    for i in des:
        name = i.text
        Description.append(name)
    # print(len(Description))

    # Ratings of the Product
    cnt = 0
    rev = box.find_all("div", class_="_3LWZlK")
    for i in rev:
        name = i.text
        Rating.append(name)
        cnt = cnt + 1
    while cnt != 24:
        Rating.append("-")
        cnt += 1
    # print(len(Reviews))
    # print(Reviews)

    # Reviews of the Product
    tot = box.find_all("span", class_="_2_R_DZ")
    for i in tot:
        name = i.text
        Reviews.append(name)
    # print(Reviews)


# Converting the Obtained values into DataFrame
df = pd.DataFrame({"Product Name": Product_Name, "Prices": Price,
                  "Description": Description, "Review": Reviews, "Rating": Rating})
# print(df)

# Making a CSV file of the obtained data
df.to_csv("Flipkart_Laptop_under_50000" + ".csv")
# For Confirmation
print("Done All the Pages")
