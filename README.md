# Scraping-bike-specifications-using-Scrapy
The goal is to scrape contents from a website using Scrapy and to save the scraped data in a csv file.
This project contains python script to scrape bike's specifications from [carandbike](https://www.carandbike.com/new-bikes/models) website.

## PRE-REQUISITES
#### 1.Anaconda Navigator 
Installation : [Anaconda](https://www.anaconda.com/)
#### 2.Scrapy
Scrapy documentation : [Scrapy](https://docs.scrapy.org/en/latest/)
- Installing scrapy using command prompt/terminal : `pip install scrapy`
- Installing scrapy using anaconda's cmd.exe prompt : `conda install -c conda-forge scrapy pylint autopep8 -y` 
#### 3. Visual Studio Code (To make any changes in the script)
Installation : [VSCode](https://code.visualstudio.com/).
#### 4. Python
Documentation : [link](https://www.python.org/)

## HOW TO USE
1. Download the whole project and save it in a folder. 
2. Open cmd.exe Prompt in anaconda.
3. To run the spider, use this command : `scrapy crawl bike`
4. To save the data in csv form : `scrapy crawl bike -o bike_dataset.csv`
5. To save the data in json format : `scrapy crawl bike -o bike_dataset.json` 

 
