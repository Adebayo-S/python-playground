from bs4 import BeautifulSoup
import requests

""" finding the price of the item in this particular page """

url = "https://www.jumia.com.ng/led-display-cordless-rechargeable-clipper-ng-888b-kiki-new-gain-mpg1666285.html"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")
# print(doc.prettify())

prices = doc.find_all(text="₦")
print(prices)
parent = prices[0].parent
strong = parent.find("strong")
print(strong)
