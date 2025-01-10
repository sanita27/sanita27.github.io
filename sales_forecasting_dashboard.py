
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the enhanced dataset
file_path = '/mnt/data/enhanced_dataset.csv'
data = pd.read_csv(file_path)

# Ensure the data is sorted by date
data['SalesDate'] = pd.to_datetime(data['SalesDate'])
data = data.sort_values('SalesDate')

# Set up Streamlit app
st.title("Sales Forecasting Dashboard")

# Sidebar filters
st.sidebar.header("Filters")
item_group = st.sidebar.selectbox("Select Item Group", options=data['ItemGroup'].unique())
date_range = st.sidebar.date_input("Select Date Range", [data['SalesDate'].min(), data['SalesDate'].max()])

# Filter data based on selections
filtered_data = data[(data['ItemGroup'] == item_group) & 
                     (data['SalesDate'] >= date_range[0]) &
                     (data['SalesDate'] <= date_range[1])]

# Display filtered data
data_display = st.checkbox("Show filtered data")
if data_display:
    st.dataframe(filtered_data)

# Line chart of sales over time
st.subheader("Sales Over Time")
plt.figure(figsize=(10, 5))
plt.plot(filtered_data['SalesDate'], filtered_data['QtySales'], label='Sales', marker='o')
plt.xlabel('Date')
plt.ylabel('Sales Quantity')
plt.title(f'Sales Trend for Item Group: {item_group}')
plt.legend()
st.pyplot(plt)

# AvgPrice distribution
st.subheader("Average Price Distribution")
plt.figure(figsize=(10, 5))
plt.hist(filtered_data['AvgPrice'], bins=20, color='skyblue', edgecolor='black')
plt.xlabel('Average Price')
plt.ylabel('Frequency')
plt.title(f'Price Distribution for Item Group: {item_group}')
st.pyplot(plt)

# Add notes section
st.subheader("Notes")
st.text_area("Add your notes here:")
