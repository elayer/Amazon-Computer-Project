## Amazon Gaming Computer Price Estimator - Overview:

* Created a model to help those looking to buy a gaming computer from Amazon make a more informed decision based on the specs of a computer.

* Scraped roughly 200 pages of gaming desktop product listing information from Amazon. 

* Engineered a few features based on the product information included in the title of a product listing. Such as features for liquid cooling and bluetooth capability.

* Began model building with Linear, Lasso, Ridge, and ElasticNet linear models, as well Random Forest regression. Then, built optimized models using Optuna with XGBoost and CatBoost regression 

* Created an API for potential clients using Flask. 


## Code and Resources Used:

**Python Version:** 3.8.5

**Packages:** numpy, pandas, scipy, requests, beautiful soup, matplotlib, seaborn, sklearn, xgboost, catboost

**Web Framework Requirements Command:** ```pip install -r requirements.txt```

## References:

* Various project structure and process elements were learned from Ken Jee's YouTube series: 
https://www.youtube.com/watch?v=MpF9HENQjDo&list=PL2zq7klxX5ASFejJj80ob9ZAnBHdz5O1t

* CatBoost Regression article: 
https://towardsdatascience.com/catboost-regression-in-6-minutes-3487f3e5b329

## Web Scraping:

Created a web scraper using Requests and Beauitful Soup. From each product listing page from Amazon, the following information was obtained:
*   Brand
*   Avg. Ratings
*   Number of Ratings
*   Processor Type
*   RAM
*   Disk Size
*   Processor Speed
*   Bluetooth
*   Liquid Cooled
*   Price

## Data Cleaning

After collecting data, I performed several steps to clean and refine the data to prepare for further processing and model building. I went through the following steps to clean and prepare the data:

* Parsed the brand name out of the general product information collected from the listings

*

## EDA
Some noteable findings from performing exploratory data analysis:

![alt text](https://github.com/elayer/Amazon-Computer-Project/blob/main/price-by-processor-type.png "Processor Type Boxplots")
![alt text](https://github.com/elayer/Amazon-Computer-Project/blob/main/price-histogram.png "Price Distribution")
![alt text](https://github.com/elayer/Amazon-Computer-Project/blob/main/price-by-RAM-boxplots.png "RAM Boxplots")
![alt text](https://github.com/elayer/Amazon-Computer-Project/blob/main/price-to-brand-lmplots.png "RAM vs. Price per Brand")

## Model Building

## Model Performance

## Productionization
