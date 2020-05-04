# Spread Of COVID-19: Analysis and Prediction

This project is  based on analysis and prediction on the impact of COVID-19. 
Following are the objectives of this project:
* Time series analysis of COVID-19 impact on global as well as all the countries separately.
* Time series forecasting of COVID-19 impact on global and in the most affected countries, i.e, US, Italy and China
* Analysis on sentiments of public on effect of COVID-19 using tweets.
* Analysis on sentiment of public on government policies imposed by authorities like: Donald Trump, CDC government, CDC emergency, NIAIDNews, WHO, etc to prevent the spread of COVID-19 in US using tweets.
* Prediction model on the impact of COVID-19  to find the results on risk of death based on the confirmed cases using features like symptoms, age, sex, country etc. Here, symptoms are categorized into cold, cough, etc with direct/indirect relation to Wuhan.



## Libraries required
* Python 3
* Pandas
* Numpy
* matplotlib
* langdetect
* ipython
* textblob
* seaborn
* keras
* tensorflow
* sklearn
* scipy
* statsmodels
* itertools

## How to run
* Go to *Results*
* Folder **Time_Series_Results : **
  * Run **TimeSeriesPlots.ipynb** to see the trend of impact of COVID-19
  * Run **TimeSeriesForecastingPlots.ipynb** to see the forecasting
  
* Folder **Sentiment_Analysis_Tweets: **
  * **Twitter-data-graphs** contains time-series plotting of number of tweets-ids per day contains the dataset from repository     [COVID-19-TweetIDs](https://github.com/echen102/COVID-19-TweetIDs) (**Note:** Do not run *timeseries-graph.ipynb*)
  * Run **sentiment_analysis.ipynb** to see the sentiments on impact of COVID-19 on the basis of number of tweets posted per       day.
  * Run **SentimentAnalysis_per_day_country _final.ipynb.ipynb** to see the sentiments on impact on COVID-19 on different         countries on the basis of number of tweets posted per day (**Note:** currently the code is based on US sentiments)
* Folder **Gov_Policies_Sentiment_Analysis: **
  * Run **Sentiment_Analysis_Govt_Tweets.ipynb** to see the sentiments on government policies with respect to government           twitter profiles mentioned in objective above.
* Folder **Prediction_Model_Results:**
  * Run **PredictBasedOnConfirmedCase.ipynb** to see the accuracy of results on experiments mentioned in the last point of         objective above.
* Folder **ImportantUser_Results**
  * Run **Important_User_Analysis.ipynb** to see the trend of tweets posted by popular users (with greater number of               followers) on per day basis.
  
*  All ***.csv*** files inside the folders mentioned above consist of cleaned and processed data
* Folders other than **Results** have the complete code with data preprocessing and cleaning (**Note:** Run at your own risk)
