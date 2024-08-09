import streamlit as st
import pickle
import matplotlib.pyplot as mtp
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

header = '''
    <!DOCTYPE html>
    <html>
    <head>
            <title>Amazon Price Predictor</title>
        <style>
            h1{
                text-align:center;
                padding:10px;
                background-color:yellow;
                border-radius:20px;
                font:bold;
                color:black;
                font-size:50px;
            }
            h2{
                text-align:left;
                color:black;
                font-size:40px;
            }
            p{
                text-align:justify;
                font-size:20px;
            }
            .stApp{
                background-color:white;
                border-radius:10px;
                border-color:black;
                border-width:2px;
                border-style:solid;
            }
        </style>
    </head>
    <body>
    <h1>Amazon Category Price Predictor</h1>'''
st.markdown(header,unsafe_allow_html=True)
body='''
    <h2>Introduction</h2>
    <p>Welcome to the Amazon Category Price Predictor! This website helps you to find out the average prices of different product categories available on Amazon e-commerece website. Using machine learning tools, it predicts prices based on product ratings and customer reviews.

Whether you're shopping, selling, or just curious, our user-friendly interface and clear graphs will help you make better decisions. Check out the price predictions and explore more insights with our Power BI dashboard. Make smarter choices with the Amazon Category Price Predictor!</p>
    <h2>Getting Started</h2>
    <p>To use the Amazon Category Price Predictor, simply navigate to the "Price Predictor" tab, select your desired product category and review count range, and click "Predict" to see the price trends. For a comprehensive analysis and deeper insights, explore the "Power BI Dashboard" tab.

Experience the power of data-driven price predictions with the Amazon Category Price Predictor, and make informed decisions with confidence!</p>
    <h2>About</h2>
    <p>Hello, my name Nagavarapu Saarvari. I am currently pursuing my engineering in AI & ML at NMAMIT Nitte<br>
    I am doing this project as a part of my "Advanced Data Science with Python" internship at DLithe</p>
    <img src='https://i.pinimg.com/736x/b5/1b/78/b51b78ecc9e5711274931774e433b5e6.jpg'>
    <a href='https://github.com/NagavarapuSaarvari/Amazon-Price-Prediction' target='_blank'>Github Repository</a><br>
    <img src='https://images.rawpixel.com/image_png_800/czNmcy1wcml2YXRlL3Jhd3BpeGVsX2ltYWdlcy93ZWJzaXRlX2NvbnRlbnQvbHIvdjk4Mi1kMS0xMC5wbmc.png'>
    <a href='https://www.linkedin.com/in/saarvari-nagavarapu-419753307/' target='_blank'>Linkedin Profile</a>
    </body>
    </html>
'''

tabs_css = """
    <style>
    .stTabs [role="tablist"] {
        background-color: #262F50;
        border-radius:8px;
        padding:20px;
    }
    .stTabs [role="tab"] {
        color: white;
        padding:20px;
    }
    .stTabs [role="tab"][aria-selected="true"] {
        border-radius:10px;
        border:5px solid red;
    }
    </style>
"""

# Inject custom CSS into Streamlit app
st.markdown(tabs_css, unsafe_allow_html=True)

home,predict,dashboard = st.tabs(['Home','Price Predictor','Power BI Dashboard'])
with home:
    st.markdown(body, unsafe_allow_html=True)


with predict:
    category = st.selectbox("Category",
                            ('Electronics','Appliances', 'Fashion','Furniture', 'Home', 'Kitchen', 'Beauty', 'Health', 'Sports', 'Fitness', 'Luggage', 'Toys', 'Baby Products', 'Automobile Products', 'Music', 'Art'))
    review_range = st.selectbox("Count of Customer Reviews",
                                ('100-200', '200-400', '400-750', '750-1000'))
    review_count_range = tuple(map(int, review_range.split('-')))
    
    # Load the model and encoder
    df = pd.read_excel('amazon_sales_cleaned.xlsx')
    encoder = LabelEncoder()
    encoder.fit(df['Category'])
    
    with open('model_pipeline.pkl', 'rb') as file:
        pipeline = pickle.load(file)
    
    

    # Function to plot predictions and return the figure and axes
    def plot_predictions(category, rating_range, review_count_range, pipeline, encoder):
        # Create a DataFrame for the input ranges
        ratings = np.linspace(rating_range[0], rating_range[1], 100)
        review_counts = np.linspace(review_count_range[0], review_count_range[1], 100)
    
        data = pd.DataFrame({
            'Category': [encoder.transform([category])[0]] * len(ratings),
            'Rating': ratings,
            'Review Count': review_counts
        })
    
        # Predict using the pipeline
        predicted_prices = pipeline.predict(data)
    
        # Plotting the results
        fig, ax = mtp.subplots(figsize=(25, 20))
        ax.plot(ratings, predicted_prices)
        ax.set_xlabel('Rating',fontsize=30)
        ax.set_ylabel('Price (in 000s)',fontsize=30)
        ax.set_title(f'Predicted Prices for "{category}"',fontsize=45)
        ax.tick_params(axis='x',labelsize=25)
        ax.tick_params(axis='y',labelsize=25)
        ax.legend()
    
        return fig

    if st.button('Predict'):
        rating_range = (1.0, 5.0)  # Adjust this as needed for your use case
        fig = plot_predictions(category, rating_range, review_count_range, pipeline, encoder)
        st.pyplot(fig)

with dashboard:
    css = '''
        <iframe title="Amazon Data Dashboard" width="200%" height="700" src="https://app.powerbi.com/reportEmbed?reportId=46a2a2a2-9f82-4ec3-bc95-b759a2cf27e2&autoAuth=true&ctid=51697115-1ecd-42b5-b509-2d62c3919f76" frameborder="0" allowFullScreen="true" style="display: block; margin-left: 0;"></iframe>
    '''
    st.markdown(css, unsafe_allow_html=True)
