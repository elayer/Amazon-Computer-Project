## Amazon Gaming Computer Price Estimator - Overview:

* Created a model to help those looking to buy a gaming computer from Amazon make a more informed decision based on the specs of a computer.

* Scraped roughly 200 pages of gaming desktop product listing information from Amazon. 

* Engineered a few features based on the product information included in the title of a product listing. Such as features for liquid cooling and bluetooth capability.

* Began model building with Linear, Lasso, Ridge, and ElasticNet linear models, as well Random Forest regression. Then, built optimized models using Optuna with XGBoost and CatBoost regression 

* Created an API for potential clients using Flask. 


## Code and Resources Used:

**Python Version:** 3.8.5

**Packages:** numpy, pandas, scipy, requests, beautiful soup, matplotlib, seaborn, sklearn, xgboost, catboost, optuna

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

* Created Liquid Cooled and Bluetooth attributes by parsing the product information for if it contained the capability for these features

* Coalesced the processor types written differently to be uniform across the data and removed any outliers 

* Reformatted the price, number of ratings, and avg. ratings columns to be appropriate numeric values. Dropped rows that had no price target variable

* Reformatted and rescaled Processor speed, RAM, and disk size to numeric values and scaled each attribute to GB

*   Removed outliers from the data that had very extreme value using <b>Z-Score</b>

* Ordinally encoded processor tpyes and dropped the records that were extremely underrepresented

* Created dummy variables for the brands of the computers that were not extremely underrepresented

## EDA
Some noteable findings from performing exploratory data analysis can be seen below. When going from a low to more high-end processor, the price of a computer does indeed increase. The same applies to RAM. In addition, I noticed some brands were priced higher even with similar or lower amounts of disk space. I eventually found that just as big of a driver in price was the brand of a computer, and not only the specs.

![alt text](https://github.com/elayer/Amazon-Computer-Project/blob/main/price-by-processor-type.png "Processor Type Boxplots")
![alt text](https://github.com/elayer/Amazon-Computer-Project/blob/main/price-histogram.png "Price Distribution")
![alt text](https://github.com/elayer/Amazon-Computer-Project/blob/main/price-by-RAM-boxplots.png "RAM Boxplots")
![alt text](https://github.com/elayer/Amazon-Computer-Project/blob/main/price-to-brand-lmplots.png "RAM vs. Price per Brand")

## Model Building
Before building any models, I transformed the categorical variables into appropriate numeric types. I transformed brand into dummy variables since some of the more expensive computers were similar in distribution of price, and the same goes for less expensive computers. I then ordinally encoded the processor types since each type seemed to have a steady increase in price as you improved the quality of the processor.

I first tried a few different linear models and some variations of them:

* Starting with Linear regression, and then trying Lasso, Ridge, and ElasticNet to see if the results would change since we have many binary columns. 

* This then led me to try Random Forest, XGBoost, and CatBoost regression because of the sparse binary/categorical nature of most of the attributes in the data. 

## Model Performance
The Random Forest, XGBoost, and CatBoost regression models respectively had improved performances. These models considerably outperformed the linear regression models I tried previously. Below are the R2 score values most recently recorded for the models:

* Linear Regression: 72.28 (the best of the linear models as a baseline)

* Random Forest Regression: 83.76

* XGBoost Regression: 85.38

* CatBoost Regression: 85.87

I used Optuna with XGBoost and CatBoost to build an optimized model especially with the various attributes that these algorithms have. Since the data used is very sparse or represent specific definitive values (categories), it makes sense that the tree-based methods perform much better. 

Since the CatBoost algorithm makes much more accurate predictions when juxtaposing mock predicted values between the Linear, Ridge, and Lasso Regression with CatBoost, I decided to keep it in the current version of this project. Although CatBoost is harder to describe as well as interpret from a non-technical perspective, I wanted to emphasize making as accurate as possible predictions with this project.

## Productionization
I created a Flask API hosted on a local webserver. For this step I primarily followed the productionization step from the YouTube tutorial series found in the refernces above. This endpoint could be used to take in certain aspects of a computer, make appropriate transformations to the variables, and return a predicted price for a computer.  

<b>UPDATE:</b> A working local Flask API simulation is now uploaded and working. Below are a few sample pictures:

![alt text](https://github.com/elayer/Amazon-Computer-Project/blob/main/amazon_homepage.png "Website Homepage")
![alt text](https://github.com/elayer/Amazon-Computer-Project/blob/main/amazon_prediction.png "Website Prediction Page")
![alt text](https://github.com/elayer/Amazon-Computer-Project/blob/main/amazon_products_example.png "Products Example")

Even though the given specs provides a good prediction for some examples (see picture above), there are also product listings that have higher and lower prices which may skew some results when making predictions. For instance, there are computers with the exact the same specs as the examples listed above with much higher prices. In the future, this could be an area of improvement for this project.

## Future Improvements
If there are any efforts in the future to improve this project, I would start with the data itself. Though, it is very difficult to obtain data by scraping amazon product listings pages in a more sophisticated way to obtain more honest and elaborate data about the product listings. Some aspects that I believe could have helped the project is improved data quality and display on Amazon, and practical points in product listings to acquire more details that could benefit model construction such as a computer's GPU. 

**I also think there are still outliers that may throw off some predictions since even products with the same base specs could have varying prices due to some other factors we can't capture with the data at hand. I could choose to return to the data itself and remove any outliers from records with similar specs across the board yet differ in price greatly. See production example for further understanding.**

In terms of model building, perhaps some advanced regression methods such as stacking or blending methods could enhance the model beyond the metrics currently obtained. Also, since there are many binary attributes making the data very sparse as well as the size of the dataset not being too large, trying an SVM could be a well-suited algorithm for this project, or a linear model with polynomial features. As it currently stands, using an ensemble tree based method won't be able to extrapolate new values if we use unseen combinations of variables when making predictions.

Having more data alone I believe would greatly improve the model as well, as well as changing the train test split proportion to allow for more data to train with since we only have so many records.

Also we could experiment with optimizing the lowest RMSE or MAE with Optuna instead of maximizing the R2 score and compare results.
