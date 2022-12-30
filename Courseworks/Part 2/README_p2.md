# **README.md file for 2**



### **External packages and libraries**



For the sake of this project various external libraries were implemented for the sake of sourcing data through APIs and enriching data. All are simple to install, so long as Python in installed and all make use of Python's package manager, pip . 

A description of their basic function and information on how they can be install is listed as follows - 



- **pandas:** This library provides data structures and data analysis tools for working with tabular data, allowing the  this assignment, 
Installed with the following command -  **pip install pandas** . 

- **matplotlib:** This library provides functions for creating various types of plots and charts. It is a powerful tool for data visualization, and is often used in conjunction with pandas to create plots of data stored in a DataFrame. Using for this project to visualise correlations between variables investigated in this report. Installed with the following command -  **pip install matplotlib.**

- **seaborn:** This library provides functions for creating more advanced and visually appealing plots, built on top of matplotlib.pyplot. Installed with the folloiwng command -  **pip install seaborn** . 

- **datetime:** This library provides classes for working with date and time data. It includes functions for parsing dates and times from strings, formatting dates and times as strings, and performing arithmetic with dates and times. Used in this project to pass in dates into functions to retrieve data within a particular time range. Installed with the following command -  **pip install datetime** . 

- **nltk, specifically SentimentIntensityAnalyzer / VADER:** This library provides tools for natural language processing tasks such as tokenization, part-of-speech tagging, and sentiment analysis. It is a comprehensive library that is widely used in the field of natural language processing. One of the key components of nltk is the SentimentIntensityAnalyzer, which is a tool for performing sentiment analysis on text data. Used specifically in this report to determine the sentiment polarity of Twitter textual data. VADER as a sentiment analyser can be install entirely by installing 'nltk', using the following - **pip install nltk** . 

- **textblob:** This library provides tools for natural language processing tasks such as tokenization, part-of-speech tagging, and sentiment analysis. TextBlob was implemented specifically in this report in order to provide polarity scores related to subjectivity as opposed to soley sentiment, so it was chosen to be implemented alongside VADER for the sentiment and subjectivity analysis of tweets. Installed in the following command, **pip install textblob** . 

- **snscrape:** This library provides tools for scraping social media data, without the need of API keys or an specialised account. It includes functions for accessing the Twitter API and downloading data from Twitter, such as tweets and user profiles, but also under a variety of search parameters like keyword, location, date of tweets, etc .. Installed with the following command - **pip3 install snscrape** . pip3 is specified because snscrape requires Python 3.8 or higher in order to run. 

- **re:** This library provides functions for working with regular expressions, which are a way of matching patterns in text. Regular expressions are often used for tasks such as searching for specific words or phrases in a document, or validating that a string conforms to a certain pattern. In the case of this project, it is used to filter out specific uncessary parts of scraped tweets and clean them, as sentiment and subjectivity scores may be inaccurate if uneccessary spaces and characters are left within the scraped tweet data. **re** is a part of the Python standard library, so it doesn not need to be installed using pip, only imported at the beginning of a script. 

- **yfinance:** This library provides access to financial data from Yahoo Finance, for this project in particular, it was implemented to retrieve adjusted closing market price data for BTC, Bitcoin, for the last 150 days from 25/12/2022. Installed using the following command - the **pip install yfinance** . 

- **scipy:** scipy: This library provides functions for scientific and technical computing tasks such as optimisation, interpolation, and statistical tests. It contains functions for performing statistical tests, two of which are implemented in the Part 2 of the SDPA assignment, the non-parametric Spearman rank correlation coefficient test (spearmanr) and the parametric Pearson correlation coefficient tes (pearsonr). Installed using the following command - **pip install scipy** . 
