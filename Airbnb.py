import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image 
import plotly_express as px

# Load Image 
img = Image.open(r"/Users/anithasmac/Downloads/airbnb.png") 
bnb = pd.read_csv('/Users/anithasmac/PycharmProjects/Airbnb/Airbnb.csv')

# Streamlit code
st.set_page_config(page_title='Airbnb Analysis', layout='wide')
st.header(':orange[Airbnb Analysis]')

with st.sidebar:
    st.sidebar.image(img)
    selected = option_menu("Menu", ["Home", "Explore Insights"], 
        icons=['house', 'bar-chart'], menu_icon="menu-button"
    )

    if selected == 'Explore Insights':
        explore_selected = option_menu(None, ["General Insights", "Filtered Insights"], 
                                icons=['graph-up', 'filter-square'])
        
if selected == 'Home':
    st.write(' ')
    st.markdown("### :blue[Domain:] Travel Industry, Property Management and Tourism")
    st.markdown("### :blue[Tools Used:] Github, Pandas, Data Preprocessing, EDA, Streamlit, Tableau")
    st.markdown("### :blue[About the Project:] This project is designed to visualize and explore Airbnb transaction and user data across various regions. It leverages several powerful tools including Streamlit for interactive web applications, Plotly for rich visualizations, and MySQL for database management. The data is sourced from JSON files that represent various metrics for different states, years, and quarters.")

if selected == 'Explore Insights':
    if explore_selected == 'General Insights':
        st.write('### General Insights')

        tab1, tab2 = st.tabs(["Geospatial Visualization", "Other Visualizations"])

        with tab1:
            # Availability and price by country 
            top_destinations = bnb.groupby('country')['availability'].sum().reset_index()
            destinations = bnb.groupby('country')['price'].mean().round(0).reset_index()
            grouped_data = pd.merge(top_destinations, destinations, on='country')
            fig1 = px.scatter_geo(
                grouped_data,
                locations='country', 
                locationmode='country names',  
                size='availability',  
                hover_name='country',  
                hover_data={'price': True, 'availability': True, 'country': False},  
                title='Availability and Average Price by Country',
                color='price',
                color_continuous_scale=px.colors.sequential.Bluered_r,
                projection="natural earth", 
                width=800, height=800
            )
            st.plotly_chart(fig1)

        with tab2:
            # Popular destinations by ratings
            top_destinations = bnb.groupby('country')['rating'].mean().round(1).sort_values(ascending=False).reset_index()
            fig2 = px.strip(top_destinations, x='country', y='rating', title='Popular Destinations by Ratings', labels={'country': 'Country', 'rating': 'Rating'})
            st.plotly_chart(fig2)

            # Total Price by property type
            bnb['total_extra_costs'] = bnb['security_deposit'] + bnb['cleaning_fee']
            grouped_data = bnb.groupby('property_type').agg({
                'price': 'mean',
                'total_extra_costs': 'mean'
            }).round().reset_index()
            fig3 = px.scatter(
                grouped_data,
                x='price',
                y='total_extra_costs',
                color='property_type',
                title='Mean Total Extra Costs (Security Deposit + Cleaning Fee) vs. Mean Price by Property Type',
                labels={'price': 'Price ($)', 'total_extra_costs': 'Total Extra Costs ($)'},
                hover_name='property_type'
            )
            st.plotly_chart(fig3)

            # Accomodation by room type
            accommodates = bnb.groupby('room_type')['accommodates'].mean().round().reset_index()
            fig4 = px.bar(accommodates, x='room_type', y='accommodates', title='People Accommodation by Room Type', labels={'room_type': 'Room Type', 'accommodates': 'Max No. Of Persons'}, color_discrete_sequence=px.colors.sequential.Oryel_r)
            st.plotly_chart(fig4)

    if explore_selected == 'Filtered Insights':
        st.write('### Filtered Insights')

        tab1, tab2 = st.tabs(["Country-Based Insights", "Property-Based Insights"])

        with tab1:
            countries = bnb['country'].unique()
            selected_countries = st.multiselect('Select Countries', countries, default=countries[:1], key='country_multiselect_tab1')

            # Apply filters
            filtered_data = bnb[(bnb['country'].isin(selected_countries))]
            # Top 10 Hosts by Reviews
            top_hosts = filtered_data.groupby(['host_name', 'country'])['number_of_reviews'].sum().sort_values(ascending=False).head(10).reset_index()
            fig1 = px.bar(top_hosts, x='host_name', y='number_of_reviews', title='Top 10 Hosts by Reviews', labels={'host_name': 'Hosts', 'number_of_reviews': 'Reviews'})
            st.plotly_chart(fig1)

            # Top property types by country
            property_type_counts = filtered_data['property_type'].value_counts().reset_index()
            fig2 = px.pie(
                property_type_counts,
                names='property_type',
                values='count',
                title='Distribution of Property Types by Country',
                labels={'property_type': 'Property Type', 'count': 'Count'}
            )
            st.plotly_chart(fig2)

        with tab2:
            countries1 = bnb['country'].unique()
            selected_countries1 = st.multiselect('Select Countries', countries1, default=countries1[:1], key='country_multiselect_tab2')

            property_types = bnb['property_type'].unique()
            selected_property_types = st.multiselect('Select Property Types', property_types, default=property_types[:3])

            filtered_data1 = bnb[bnb['country'].isin(selected_countries1) & (bnb['property_type'].isin(selected_property_types))]

            # Accommodates vs Price by Property Type
            fig3 = px.scatter(filtered_data,
                            x='accommodates',
                            y='price',
                            color='property_type',
                            title='Accommodates vs Price by Property Type',
                            labels={'accommodates': 'Number of Accommodates', 'price': 'Price ($)'},
                            hover_name='property_type',
                            height=600, width=800
                            )
            st.plotly_chart(fig3)




