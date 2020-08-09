# IMDBscraping
# Project Title

This project will gather the some information of Top 250 movies in IMDB. Information such as Title, Data, Cetificate rates, Duration time, Rating, Number of participants in rating and Director's name.

## Getting Started

Python 3.x is required to run this code.

### Prerequisites

It is preferable to run this code in virtual environment [venv] (https://docs.python.org/3/tutorial/venv.html).

```python
python -m venv foo-env
```

### Installing

This web scraping script is based on Scrapy library. Thus it reuqires to install this library via the package manager [pip](https://pip.pypa.io/en/stable/) or [Anaconda](https://www.anaconda.com/)


```
pip install scrapy
```

## Deployment

After preparing the requisites via below command, the data can be extracted. 

```
scrapy crawl IMDBtop250 -o filename.csv
scrapy crawl IMDBtop250 -o filename.json
```

## Built With

* [scrapy](https://scrapy.org/) - The python Web Crawling Library


## Authors

* **Pooria Taghdiri** - *Initial work* - (https://twitter.com/PooriaTaghdiri)



