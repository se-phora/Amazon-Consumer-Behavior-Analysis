import pandas as pd
import streamlit as st
import plotly.express as px
from interface.constants import amazon_color_palette
from interface.constants import plot_margin

def display_gender_distribution(df_clean):

    gender_count = df_clean['Gender'].value_counts(normalize=True).reset_index()
    gender_count.columns = ['Gender', 'Percentage']

    fig = px.pie(
        gender_count,
        values='Percentage',
        names='Gender',
        title="Survey Respondents Are Mostly Women",
        color_discrete_sequence=amazon_color_palette,
        hole=0.4,
        custom_data=["Percentage"]  
    )

    fig.update_traces(
        textinfo='label+percent',
        textposition='inside',
        hovertemplate="%{customdata[0]:.0%}"  
    )

    fig.update_layout(
        title_font_size=24,
        showlegend=False,
	margin=plot_margin
    )

    st.plotly_chart(fig, use_container_width=True)
