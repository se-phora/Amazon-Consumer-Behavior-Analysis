import pandas as pd
import streamlit as st
import plotly.express as px
from interface.constants import amazon_color_palette
from interface.constants import plot_margin

def display_age_group_distribution(df_clean):

    age_group_count = df_clean["age_group"].value_counts(normalize=True).sort_index().reset_index()
    age_group_count.columns = ["age_group", "percentage"]

    fig = px.bar(
        age_group_count,
        x="age_group",
        y="percentage",
        title="70% of Respondents Are Under 35",
        labels={"age_group": "Age Group", "percentage": ""},
        color_discrete_sequence=["#FF9900"],
        custom_data=["percentage"]  
    )

    fig.update_traces(
        hovertemplate="%{x}: %{customdata[0]:.0%}"
    )

    fig.update_layout(
        title_font_size=24,
        xaxis_title="",
        yaxis_tickformat=".0%",    
        yaxis_title="",
	margin=plot_margin          
    )

    st.plotly_chart(fig, use_container_width=True)
