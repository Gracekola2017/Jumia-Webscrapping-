import requests
import re
from bs4 import BeautifulSoup
import csv

url = "https://www.jumia.co.ke/"
response = requests.get(url)
# print(response)

# if response.status_code == 200:
soup = BeautifulSoup(response.content, "html.parser")
products = soup.select("div.sku.-gallery")

print(products)

data = []

for product in products:
    name = product.find("span", class_="name").text
    brand = product.find("span", class_="brand").text
    reviews = product.find("span", class_="reviews").text
    rating = product.find("span", class_="rating").text
    price = product.find("span", class_="price").text.replace(",", "").replace("Ksh", "")
    discount = product.find("span", class_="discount")
    if discount: 
        discount = discount.text.replace("-", "").replace("%", "")
    else:
        discount = "0"

        data.append({"name": name, "brand": brand, "price": price, "discount": discount, "reviews": reviews, "rating": rating})

        def save_data(data, filename):
            with open(filename, "w") as f:
                writer = csv.writer(f)
                writer.writerow(["name", "brand", "price", "discount", "reviews", "rating"])

                for item in data:
                    writer.writerow([item["name"], item["brand"], item["price"], item["discount"], item["reviews"], item["rating"]])

    def read_data(filename):
        with open(filename, "r") as f:
    
            reader = csv.reader(f)

            for row in reader:
                name, brand, price, discount, reviews, rating = row

                print(f"Name: {name}")
                print(f"Brand: {brand}")
                print(f"Price: {price} KSh")
                print(f"Discount: {discount} %")
                print(f"Reviews: {reviews}")
                print(f"Rating: {rating} / 5")
                print()

    



