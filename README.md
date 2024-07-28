# Airbnb Analysis

## Project Overview
This project provides a comprehensive analysis of Airbnb data, offering both general and filtered insights through interactive visualizations. It helps in understanding the trends and patterns in the Airbnb market, aiding in better decision-making for hosts and travelers alike.

## Tools Used
- **Pandas**
- **Data Preprocessing**
- **Exploratory Data Analysis (EDA)**
- **Streamlit**
- **Tableau**

## About the Project
This project allows users to visualize and explore Airbnb data, including availability, price, rating, property type, room type, host details, and extra costs like security deposit and cleaning fee. The application provides both general insights and filtered insights based on user selections.

## Installation and Setup

### Prerequisites
- Python 3.7 or higher
- Required Python packages: plotly, streamlit, pandas, ast, PIL
- Tableau Public
  
### Step-by-Step Guide

1. **Clone the Repository**
   ```bash
   git clone <repository_url>
    ```
2. **Install the required Python packages as listed in Prerequisites**:
    ```bash
    pip install -r required packages
    ```
3. **Run the Streamlit Application**   
    ```bash
    streamlit run Airbnb.py
    ```

## Project Components
1. Home Page
 The home page provides an introduction to the project and the tools used. It includes the following sections:

  - Domain: Travel Industry, Property Management, and Tourism
  - Tools Used: Lists the tools and technologies utilized in the project
  - About the Project: A brief description of the project's goals

2. Explore Insights
 The Explore Insights section is divided into two parts: General Insights and Filtered Insights.

- General Insights
This section provides a broad overview of the data with the following visualizations:

  Geospatial Visualization:
  Availability and Price by Country: A scatter geo plot showing the availability and average price by country.
  
  Other Visualizations:
  Popular Destinations by Ratings: A strip plot showing the popular destinations based on ratings.
  Total Price by Property Type: A scatter plot showing the mean total extra costs (security deposit + cleaning fee) vs. mean price by property type.
  Accommodation by Room Type: A bar chart showing the average number of people that can be accommodated by room type.

- Filtered Insights
This section allows users to filter the data by country and property type to gain more specific insights. It includes the following visualizations:

  Country-Based Insights:
  Top 10 Hosts by Reviews: A bar chart showing the top 10 hosts by the number of reviews.
  Distribution of Property Types by Country: A pie chart showing the distribution of property types for the selected countries.
  
  Property-Based Insights:
  Accommodates vs Price by Property Type: A scatter plot showing the relationship between the number of accommodates and price for selected property types and countries.
