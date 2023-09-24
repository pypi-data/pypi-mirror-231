# Nike ID Scraper

A Python package for scraping detailed product information from the Nike Indonesia website.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Directory Structure](#directory-structure)
- [Contributing](#contributing)
- [License](#license)

## Installation

To use this package, you need to install it in your Python environment. You can do this using pip:

```bash
pip install nikeidscraper
```

This package has the following dependencies:

pandas>=2.1
httpx>=0.25.0
playwright>=1.38.0
selectolax>=0.3.16
These dependencies will be automatically installed when you install 'nikeidscraper'.

## Usage 

### Scraping a Single Product
You can scrape data for a single Nike product using the provided main.py script as below:

```bash
import asyncio
from src.spider.scraping_result import ProductScraperHandler

async def main():
    # User input for scraping one product
    target_url_one = "product_url" # change with product url you want to scrape
    txt_file_name = "Product Name.txt" # change with the name of nike product you want to scrape

    await ProductScraperHandler.one_product(target_url_one, txt_file_name)

if __name__ == "__main__":
    asyncio.run(main())
```
 
#### Example Scraping a Single Product
Here's an example of how to use it. Scraping detail data of Air Jordan 1 Mid SE with the url: 
```bash
https://www.nike.com/id/t/air-jordan-1-mid-se-shoes-p48zQ5/DX4332-700
```

So...the code for scraping as below.

```bash
import asyncio
from src.spider.scraping_result import ProductScraperHandler

async def main():
    # User input for scraping one product
    target_url_one = "https://www.nike.com/id/t/air-jordan-1-mid-se-shoes-p48zQ5/DX4332-700"
    txt_file_name = "Air Jordan 1 Mid SE.txt"

    await ProductScraperHandler.one_product(target_url_one, txt_file_name)

if __name__ == "__main__":
    asyncio.run(main())
```

### Scraping Multiple Product
You can scrape data for some Nike products using the provided main.py script as below:

```bash
import asyncio
from src.spider.scraping_result import ProductScraperHandler

async def main():
    # User input for scraping multiple products
    target_url_multi = "multi_product_url" # change with url you want to scrape
    csv_file_name = "Multi Product Category Name.csv" # change with multi product you want to scrape as appears on the site
    product_count = 13 # change with multi product count you want to scrape as appears on the site
    timeout_seconds = 10 # If you fail to scrape due to exceed timeout, change with higher than 10 

    await ProductScraperHandler.multi_product(target_url_multi, csv_file_name, product_count, timeout_seconds)

if __name__ == "__main__":
    asyncio.run(main())
```
 
#### Example Scraping Multi Product
On nike.com/id navbar you choose Men > Football > Shop by price Over Rp3.000.000, so below the data will be display
on the site:
```bash
- URL : https://www.nike.com/id/w/mens-3000000-football-shoes-1gdj0zaam0qznik1zy7ok
```
- Multi Product Category Name : Men's Over Rp3.000.000 Football Shoes
- Product count : 11

And the code for scraping as below.

```bash
import asyncio
from src.spider.scraping_result import ProductScraperHandler

async def main():
    # User input for scraping multiple products
    target_url_multi = "https://www.nike.com/id/w/mens-3000000-football-shoes-1gdj0zaam0qznik1zy7ok" 
    csv_file_name = "Men's Over Rp3.000.000 Football Shoes.csv" 
    product_count = 11 
    timeout_seconds = 10 

    await ProductScraperHandler.multi_product(target_url_multi, csv_file_name, product_count, timeout_seconds)

if __name__ == "__main__":
    asyncio.run(main())
```

#### WARNING
Make sure double quotation mark (" ") for url, .txt for single product file name, .csv for multi product file name.

### Scraping Result
The scraping result will be saved in the 'result' directory/ folder.

## Directory Structure
Directory structure of the package as below:

```bash
nike_id_scraper/
  ├── result/
  ├── src/
  │   ├── spider/
  │   │   ├── __init__.py
  │   │   ├── scraping_result.py
  │   │   ├── spider_links.py
  │   │   └── spider_product.py
  │   ├── main.py
  ├── .gitignore
  ├── LICENSE
  ├── README.md
  ├── setup.py
```

## Contributing
If you'd like to contribute to this project, please follow these steps:

- Fork the repository on GitHub.
- Create a new branch with a descriptive name.
- Make your changes and commit them.
- Push your changes to your fork.
- Submit a pull request to the original repository.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
