from aliexpress import Aliexpress
def main() -> None:

    product_name = "auriculares"

    api = Aliexpress(product=product_name)
    api.scrape_products()
    api.export_excel()

if __name__ == "__main__":
    main()