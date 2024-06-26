import requests
from bs4 import BeautifulSoup
import re

headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'}

# Define the URL of the product page
url = 'https://www.hepsiburada.com/nyx-professional-makeup-duck-plump-dolgun-gorunum-veren-dudak-parlaticisi-06-brick-of-time-pm-HBC00005SD3V7'

# Send a GET request to the URL
response = requests.get(url, headers=headers)
content = response.text

# Parse the HTML content of the page using Beautiful Soup
soup = BeautifulSoup(response.content, "lxml")

# Extract the product name
product_name = soup.find("h1", attrs={"class":"product-name best-price-trick"}).text.strip()

# Extract the product brand
product_brand = soup.find("span", attrs={"class":"brand-name"}).text.strip()

# Extract the product price
product_price = soup.find("div", attrs={"class":"originalPriceContainer product-old-price hidden"}).text.strip()
product_price = product_price.rstrip("%0")  # Remove "%0" from the end of the product_price string

# Extract the product seller
product_seller = soup.find("a", attrs={"data-bind":"text: product().currentListing.merchantName, attr: { href: product().currentListing.merchantPageUrl, 'data-hbus': userInformation() && userInformation().userId && isEventReady() ? productDetailHbus('GoToSellerClick' ): ''}"}).text.strip()

# Extract the product rating
product_rating = soup.find("span", attrs={"class":"hermes-AverageRateBox-module-g3di4HmmxfHjT7Q81WvH"}).text.strip()

# Extract the product reviews count
product_reviews_count = soup.find("div", attrs={"id":"comments-container"}).text.strip()

# Extract the product description
product_description = soup.find("div", attrs={"id":"productDescriptionContent"}).text.strip()
# re.sub(pattern, repl, string, count=0, flags=0)
product_description = re.sub(r'&Nbsp;', '', product_description)  # Remove "&Nbsp;" characters
"""
# Extract the product reviews
reviewer1 = soup.find("span", attrs={"class":"hermes-ReviewCard-module-ooww5HUvW5kp0ULoZFyH"}).text.strip()
review1 = soup.find("div", attrs={"class":"hermes-ReviewCard-module-KaU17BbDowCWcTZ9zzxw"})
product_review1 = review1.find("span", attrs={"itemprop":"description"}).text.strip()

reviewer2 = soup.find("div", attrs={"class":"hermes-ReviewCard-module-ba888_vGEW2e_XKxTgdA"}).text.strip()
review = soup.find("div", attrs={"class":"hermes-ReviewCard-module-dY_oaYMIo0DJcUiSeaVW"})
review2 = review.find("div", attrs={"class":"hermes-ReviewCard-module-KaU17BbDowCWcTZ9zzxw"})
product_review2 = review2.find("span", attrs={"itemprop":"description"}).text.strip()
"""

reviewers = soup.find_all("span", attrs={"class":"hermes-ReviewCard-module-ooww5HUvW5kp0ULoZFyH"})
reviews = soup.find_all("div", attrs={"class":"hermes-ReviewCard-module-KaU17BbDowCWcTZ9zzxw"})

print('Product Name:', product_name)
print('Product Brand:', product_brand)
print('Product Price:', product_price)
print('Product Seller:', product_seller)
print('Product Rating:', product_rating)
print('Product Reviews Count:', product_reviews_count)
print('Product Description:', product_description)

"""
print('First Reviewer:', reviewer1)
print('Product First Review:', product_review1)
print('First Reviewer:', reviewer2)
print('Product Second Review:', product_review2)
"""

"""
# Print reviewers one by one
for reviewer in reviewers:
    print('Reviewer:', reviewer.text.strip())

# Print each review one by one
for review in reviews:
    review_text = review.find("span", itemprop="description").text.strip()
    print('Review:', review_text)
"""

# Print reviewers and their reviews sequentially
for i in range(min(len(reviewers), len(reviews))):
    reviewer = reviewers[i].text.strip()
    review = reviews[i].find("span", itemprop="description").text.strip()
    print('Reviewer:', reviewer)
    print('Review:', review)
    print()  # Add an empty line for better readability between reviews
