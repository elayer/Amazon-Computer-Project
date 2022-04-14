## Amazon Gaming Computer Price Estimator - Overview:

* Created a model to help those looking to buy a gaming computer from Amazon make a more informed decision based on the specs of a computer.

* Scraped roughly 200 pages of gaming desktop product listing information from Amazon. 

* Engineered a few features based on the product information included in the title of a product listing. Such as features for liquid cooling and bluetooth capability.

* Began model building with Linear, Lasso, Ridge, and ElasticNet linear models, as well Random Forest regression. Then, built optimized models using Optuna with XGBoost and CatBoost regression 

* Created an API for potential clients using Flask. 


## Code and Resources Used:

<b>Python Version</b>: 3.8.5

<b>Packages</b>: numpy, pandas, scipy, requests, beautiful soup, matplotlib, seaborn, sklearn, xgboost, catboost

<b>Web Framework Requirements Command</b>: pip install -r requirements.txt

## References:

* Various project structure and process elements were learned from Ken Jee's YouTube series: https://www.youtube.com/watch?v=MpF9HENQjDo&list=PL2zq7klxX5ASFejJj80ob9ZAnBHdz5O1t

* CatBoost Regression article: https://towardsdatascience.com/catboost-regression-in-6-minutes-3487f3e5b329

## Web Scraping:

Created a web scraper using Requests and Beauitful Soup. From each product listing page from Amazon, the following information was obtained:
* Brand

* Avg. Ratings

* Number of Ratings

* Processor Type

* RAM

* Disk Size

* Processor Speed

* Bluetooth

* Liquid Cooled

* Price
