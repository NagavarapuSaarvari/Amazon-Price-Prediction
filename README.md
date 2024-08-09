# Introduction
**The Amazon Price Predictor** is a data analysis and machine learning tool that is used to predict the average price of various product categories available on the amazon e-commerece website.It can be helpful for the people who are planning to invest a huge amount and purchase a lot of items. Using this tool, the users can understand the performance and quality of the products sold on the website throughout the year as the dataset used for building the model was scrapped from the amazon webiste.

# Getting Started
On opening the wesite, we will have 3 tabs.

**Home:** This tab contains the introduction to the website, a user guide for navigating through the webiste and an about section consisting the links to the github repository and my linkedin profile

**Price Predictor:** It contains 2 dropdown lists. One is to select the category and the other is to select the range of review counts. On pressing the predict button after selecting the two parameters, a graph is plotted which shows the prices of the products on y-axis and ratings on the x-axis. This shows the performance of the products across different rating and product ranges

**Power BI Dashboard:** This tab shows the Power BI Dashboard which was built on the scrapped dataset

# Programming Languages Used
1) Python
2) HTML and CSS for the website

## Python Packages Used
1) Pandas
2) Numpy
3) BeautifulSoup 4
4) Scikit-Learn
5) Matplotlib
6) Pickle
7) Streamlit

## Setup
Firstly, install the requirements using the command **`pip install -r requirements.txt`**

Then install the beautifulsoup4 and pickle packages in the jupyter notebook using the **`pip install [package_name]`** command.

## Deployment
Run the website on your loacal host using the command **`streamlit run Website.py`** in the command prompt
