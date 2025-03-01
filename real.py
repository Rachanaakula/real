import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Sample real estate data
data = {
    "Property Name": ["House A", "House B", "House C", "House D", "House E"],
    "Location": ["New York", "San Francisco", "Los Angeles", "Austin", "Chicago"],
    "Price": [500000, 750000, 400000, 300000, 600000],
    "Bedrooms": [3, 4, 2, 3, 4],
    "Bathrooms": [2, 3, 2, 2, 3],
    "Area (sq ft)": [2500, 3500, 2200, 1800, 2800],
    "Type": ["Detached", "Semi-Detached", "Condo", "Detached", "Townhouse"]
}

# Create a dataframe from the sample data
df = pd.DataFrame(data)

# Title of the app
st.title('Real Estate Dashboard')

# Display data
st.subheader('Property Listings')
st.dataframe(df)

# Sidebar for filtering
st.sidebar.header('Filter Properties')

# Price Filter
min_price, max_price = st.sidebar.slider(
    'Price Range', 
    min_value=int(df['Price'].min()), 
    max_value=int(df['Price'].max()), 
    value=(int(df['Price'].min()), int(df['Price'].max()))
)

# Filter the dataframe based on price
filtered_df = df[(df['Price'] >= min_price) & (df['Price'] <= max_price)]

# Bedrooms filter
bedrooms = st.sidebar.selectbox('Number of Bedrooms', options=df['Bedrooms'].unique(), index=0)

# Filter by bedrooms
filtered_df = filtered_df[filtered_df['Bedrooms'] == bedrooms]

# Property Type filter
property_type = st.sidebar.selectbox('Property Type', options=df['Type'].unique(), index=0)

# Filter by property type
filtered_df = filtered_df[filtered_df['Type'] == property_type]

# Display the filtered data
st.subheader(f'Filtered Listings (Price Range: ${min_price} - ${max_price}, Bedrooms: {bedrooms}, Type: {property_type})')
st.dataframe(filtered_df)

# Price Distribution Chart
st.subheader('Price Distribution')
plt.figure(figsize=(10, 6))
plt.hist(df['Price'], bins=10, color='skyblue', edgecolor='black')
plt.title('Price Distribution of Properties')
plt.xlabel('Price')
plt.ylabel('Frequency')
st.pyplot()

# Price vs Area Scatter Plot
st.subheader('Price vs Area (sq ft)')
plt.figure(figsize=(10, 6))
plt.scatter(df['Area (sq ft)'], df['Price'], color='orange')
plt.title('Price vs Area')
plt.xlabel('Area (sq ft)')
plt.ylabel('Price')
st.pyplot()
