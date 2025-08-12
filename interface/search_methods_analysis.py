import pandas as pd
import streamlit as st
import plotly.express as px
from interface.constants import plot_margin

def display_search_methods(df_clean):

    search_method = df_clean["Product_Search_Method"].value_counts(normalize=True).reset_index()
    search_method.columns = ['Search Method', 'Percentage']

    fig = px.bar(
        search_method,
        x='Search Method',
        y='Percentage',
        title="Most Users Search by Categories and Keywords",
        color_discrete_sequence=['#CC5500']
    )

    fig.update_layout(
        xaxis_tickangle=45,
        title_font_size=24,
        yaxis_tickformat=".0%",  
        yaxis_title="",
        xaxis_title="",
	margin=plot_margin  
    )

    fig.update_traces(
	hovertemplate='%{y:.0%}<extra></extra>'
    )

    st.plotly_chart(fig, use_container_width=True)
