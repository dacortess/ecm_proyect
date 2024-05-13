from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import time
import re
import os

class Aliexpress():

    def __init__(self, *, product) -> None:
        self.product: str = product.lower()
        self.products: dict = dict()
        self.index: int = 1

        self.url: str = None
        self.soup: BeautifulSoup.soup = None
        self.container: list[str] = None

        self.set_up_soup()
    
    def set_up_soup(self) -> None:
        self.url = f"https://www.aliexpress.com/w/wholesale-{self.product}.html?spm=a2g0o.productlist.auto_suggest.1"
        self.soup = BeautifulSoup(urlopen(self.url), "html.parser")
        self.container = self.soup.find_all("div", {"class": "list--gallery--C2f2tvm search-item-card-wrapper-gallery"})

    def get_title(self, *, item) -> str:
        raw_title = item.find("h3", {"class": "multi--titleText--nXeOvyr"})
        return raw_title.text
    
    def get_price(self, *, item) -> float:
        raw_price = item.find_all("div", {"class": "multi--price-sale--U-S0jtj"})
        return float("".join(re.findall('>([\s\S+]+?)</span>', str(raw_price))[1::]).replace(",", ""))
    
    def get_stars(self, *, item) -> int:
        raw_stars = item.find_all("div", {"class": "multi--progress--2E4WzbQ"})
        return [True if float(re.findall('\"width:([\s\S+]+?)px\"', str(star))[0]
                                                        ) == 10.0 else False for star in raw_stars].count(True)

    def get_sales(self, *, item) -> int:
        raw_sales = item.find("span", {"class": "multi--trade--Ktbl2jB"})
        return int(re.sub("[^0-9]", "", str(raw_sales)))
    
    def get_shipping(self, *, item) -> int:
        raw_shipping = item.find("span", {"class": "tag--text--1BSEXVh tag--textStyle--3dc7wLU multi--serviceStyle--1Z6RxQ4"})
        shipping = re.sub("[^0-9.]", "", str(raw_shipping.text))
        return  0 if shipping == "" else shipping
    
    def get_store(self, *, item) -> str:
        raw_shop = item.find("span", {"class": "cards--store--3GyJcot"})
        return raw_shop.text
    
    def get_images(self, *, item) -> list[str]:
        raw_imgs = item.find_all("img", {"class": "images--item--3XZa6xf"})
        return [re.findall('src=\"([\s\S+]+?jpg)\"', str(img)) for img in raw_imgs]

    def export_excel(self):
        df = pd.DataFrame(data=self.products).transpose()
        
        file_name = f"products_{self.product}_{round(time.time() * 1000)}"
        path = os.path.join('results', f'{file_name}.xlsx')

        df.to_excel(path)

    def scrape_products(self):
        for item in self.container:
            self.products[self.index] = dict()

            self.products[self.index]["Title"] = self.get_title(item = item)
            self.products[self.index]["Price"] = self.get_price(item = item)
            self.products[self.index]["Stars"] = self.get_stars(item = item)
            self.products[self.index]["Sales"] = self.get_sales(item = item)
            self.products[self.index]["Shipping"] = self.get_shipping(item = item)
            self.products[self.index]["Store"] = self.get_store(item = item)
            self.products[self.index]["Images"] = self.get_images(item = item)

            self.index += 1
