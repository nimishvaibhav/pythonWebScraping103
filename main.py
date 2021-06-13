import requests
from bs4 import BeautifulSoup


def get_page(url):
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"}
    response = requests.get(url, headers=header)

    return response


def get_page_content(response):
    soup = BeautifulSoup(response.content, 'lxml')
    product_name = soup.find(id='productTitle').text.strip()
    price = soup.find(id='priceblock_ourprice').text
    stock = soup.find(id='availability').text.strip()
    print(product_name, price, stock)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    url = 'https://www.amazon.in/New-Apple-iPhone-12-128GB/dp/B08L5TNJHG/ref=sr_1_2?dchild=1&keywords=iphone12&qid=1622972505&sr=8-2'
    response = get_page(url)
    get_page_content(response)

