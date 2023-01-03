# README.md file
Link to assignment GitHub repository - https://github.com/MurasatoNaoya/ft22584_EMATM0048

## **Part 1 of SDPA assignment**


### **Project description -**
This project is a proof-of-concept banking system that uses three pre-defined classes and their defined functionality in the way of methods, for its simulation. Users are able to create accounts, manage their accounts through the creation of wallets and interact between their wallets and other customers; where applicable, as they see fit. It must be noted that as this is a proof-of-concept program, no real money is deposited to wallets and therefore users of the application can deposit money as they see fit, as there is not external link to any real source of money.

### **Files / class(es) used in the application & design choices and justifications -**


#### **BankingSystem** 
The BankingSystem class defined within the BankingSystem.py file serves as the orchestrator class, in the sense that it is responsible for coordinating the interaction and flow of data between the other classes used in the banking system application, acting as a central point of control for managing the execution of tasks and processes. Most the of the functions that relate to the system itself, like interface displays (e.g customer creation screen, or wallet management menu), login functionality and functions that relate to the manipulation of Customer class instances (create account, delete account, select account, etc..) are defined in the BankingSystem class. 

With regards to design decisions, a key point to mention is that the BankingSystem class is where individual instances of the Customer class, and therefore where all internal customer data is stored. Therefore, for the sake of maintaining a legible and understandable architecture, it was important that any function that makes use of attributes from instances of the Customer class stored in the dictionary customers, should be within the BankingSystem class for ease of retrieval. 

##### **Encryption method in BankingSystem class** -
The savings of key customer information (username and password) to a local .csv file and the encryption of the passwords defined as the method _saver_encrypter_ was chosen to be implemented within the BankingSystem class largely because of how the functionality related to the system itself, not to the actions of any customer or properties of any particular wallet. It would make more sense of the system itself to save the key information and encrypt the passwords, hence its placement in the BankingSystem class. The implementation of encryption in the BankingSystem class is that of substitution using a specific cipher specified within the _saver_encrypter_ method. For the sake of this banking application in particular, a method of encryption via substitution was chosen for the following reasons - 

- Substitution encryption is generally very fast, as it does not require any complex mathematical operations or large amounts of data to be processed. This makes it a good choice for applications where speed is important. Although proof of concept, latency and general speed of operation is an extremely important factor for consumer banking, so a computationally less intensive means of encryption may be more viable.

- Substitution encryption is secure, so long as the mapping between the original characters and the encrypted characters is kept secret, meaning that the encryption can be very difficult to break, even if an attacker knows the general structure of the cipher. Substitution encryption is vulnerable to frequency attacks, where an attacker can use the known frequency of characters in a language to try and determine the mapping of the substitution cipher. For example, if the letter 'a' is the most common letter in the English language, an attacker could guess that the most common ciphertext letter corresponds to 'a'. Similarly, substitution encryption is also vulnerable to brute force attacks, where an attacker tries all possible combinations of the substitution cipher until the correct one is found. However, the strength of substitution encryption lies in the fact that the distribution of the cipher is constant, meaning that the frequency of characters in the ciphertext is the same as the frequency of characters in the plaintext. This can make it difficult for an attacker to determine the mapping of the substitution cipher based on frequency alone, since all possible combinations of the substitution cipher will have the same frequency distribution.

The particular substitution cipher implemented in the banking system has been deemed to balance the trade-off between the robustness of encryption and algorithmic complexity / run time and so has been selected for this preliminary application. More sophisticated cryptographic means of encryption may also have to be considered for future iterations of the application. 


#### **Customer** 
The Customer class defined with the Customer.py file serves as the class that stores the information associated with the specific accounts a given Customer / instance of the Customer class and allows that information to be manipulated, added to or taken away from - in the case of this banking application specifically, this manipulation is wholly related to the creation, management and display of wallets. In summary, this class account for the management of customer information and assets in relation any one specific customer, for all methods excluding core wallet functionality, (e.g, create wallet, delete wallet, display wallets, etc..) .

In a similar sense to the orchestrator class BankingSystem, it was important to design the Customer class such that methods using attributes associated with the dictionary 'wallets' stored within the Customer class be implemented within there, to allow for easy access to the attributes, rather than having to pass another class containing the 'wallets' attributes as a parameter for every method. 


#### **Wallets** 
The wallet classes defined within the Wallets.py file serve as the classes that define that available functionality of each wallet type and the attributes that vary in response to methods related to customer action, (e.g, last_transaction, balance, etc..) .

Because of how all wallet types support functionality for the customer to deposit money into it, a base class containing the generalised attributes of all wallets and a method for depositing funds was defined, and then that class was inherited by all of the wallets types available in the banking system in the form of child classes. Additional functionality for withdrawals and transfers were also added to wallets of applicable wallet type.


#### **main()** 
The main function defined within the main.py file finally serves as means of organising the defined functions specified within their respective classes, into a coherent logical banking system. 

The main consideration made for the design of the main() function was about how to break out of several while loops when a certain decision was made; largely to return to the main menu. A simple break statement would be insufficient most of the time, as the depth of the program was greater than 1, and therefore a would not be able to return to the base while loop with a single break statement. To solve this, several Boolean conditions from a-f were defined such that if the logic deemed the breaking of loops from a place where depth >1, it could do so by changing the Boolean statements determining the operation of a given while loop to False, allowing breaks of multiple indentation to happen. 






## **Part 2 of SDPA assignment**


### **External packages and libraries -**
In the Part 2 of this SDPA assignment, various external libraries were implemented for the sake of sourcing data through APIs and enriching data. All are simple to install, so long as Python in installed and all make use of Python's package manager, pip . A description of their basic function, and information on how they can be installed is listed as follows -

- **pandas:** This library provides data structures and data analysis tools for working with tabular data, allowing for the formatting and investigation of the data scraped for this assignment. Installed with the following command - **pip install pandas** .

- **matplotlib:** This library provides functions for creating various types of plots and charts. It is a powerful tool for data visualisation, and is often used in conjunction with pandas to create plots of data stored within DataFrames. Using for this project to visualise correlations between variables investigated in this report. Installed with the following command - **pip install matplotlib.** 

- **seaborn:** This library provides functions for creating more advanced and visually appealing plots, built on top of matplotlib.pyplot. Installed with the following command - **pip install seaborn** . 

- **datetime:** This library provides classes for working with date and time data. It includes functions for parsing dates and times from strings, formatting dates and times as strings, and performing arithmetic with dates and times. Used in this project to pass in dates into functions to retrieve data within a particular time range. Installed with the following command 

- **datetime** is a part of the Python standard library, so it does not need to be installed using pip, only imported at the beginning of a script.

- **nltk, specifically SentimentIntensityAnalyzer / VADER:** This library provides tools for natural language processing tasks such as tokenization, part-of-speech tagging, and sentiment analysis. It is a comprehensive library that is widely used in the field of natural language processing. One of the key components of nltk is the SentimentIntensityAnalyzer, which is a tool for performing sentiment analysis on text data. Used specifically in this report to determine the sentiment polarity of Twitter textual data. VADER as a sentiment analyser can be install entirely by installing 'nltk', using the following - **pip install nltk** . 

- **textblob:** This library provides tools for natural language processing tasks such as tokenization, part-of-speech tagging, and sentiment analysis. TextBlob was implemented specifically in this report in order to provide polarity scores related to subjectivity as opposed to solely sentiment, so it was chosen to be implemented alongside VADER for the sentiment and subjectivity analysis of tweets. Installed in the following command, **pip install textblob** . 

- **snscrape:** This library provides tools for scraping social media data, without the need of API keys or a specialised account. It includes functions for accessing the Twitter API and downloading data from Twitter, such as tweets and user profiles, but also under a variety of search parameters like keyword, location, date of tweets, etc… Installed with the following command - **pip3 install snscrape** . pip3 is specified because snscrape requires Python 3.8 or higher in order to run.

- **re:** This library provides functions for working with regular expressions, which are a way of matching patterns in text. Regular expressions are often used for tasks such as searching for specific words or phrases in a document, or validating that a string conforms to a certain pattern. In the case of this project, it is used to filter out specific unnecessary parts of scraped tweets and clean them, as sentiment and subjectivity scores may be inaccurate if unnecessary spaces and characters are left within the scraped tweet data. **re** is a part of the Python standard library, so it does not need to be installed using pip, only imported at the beginning of a script. 

- **yfinance:** This library provides access to financial data from Yahoo Finance, for this project in particular, it was implemented to retrieve adjusted closing market price data for BTC, Bitcoin, for the last 150 days from 25/12/2022. Installed using the following command - the **pip install yfinance** . 

- **scipy:** scipy: This library provides functions for scientific and technical computing tasks such as optimisation, interpolation, and statistical tests. It contains functions for performing statistical tests, two of which are implemented in the Part 2 of the SDPA assignment, the non-parametric Spearman rank correlation coefficient test (spearmanr) and the parametric Pearson correlation coefficient test (pearsonr). Installed using the following command - **pip install scipy** . 
