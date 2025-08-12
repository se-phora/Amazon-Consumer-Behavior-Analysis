import pandas as pd
import streamlit as st
import plotly.express as px
from interface.constants import plot_margin


def display_cart_abandonment(df_clean):
    
    cart_abandonment = df_clean["Cart_Abandonment_Factors"].value_counts(normalize=True)

    chart_data = pd.DataFrame({
        "Raisons": cart_abandonment.index,
        "Percentage": cart_abandonment.values
    })

    fig = px.bar(
        chart_data,
        x="Percentage",
        y="Raisons",
        orientation="h",
        color_discrete_sequence=["#FF9900"],
    	custom_data=["Percentage"]
    )
    fig.update_traces(
	hovertemplate="%{customdata[0]:.0%}"
    )

    fig.update_layout(
        title="Top Reasons for Cart Abandonment",
	title_font_size=24,
	xaxis_tickformat=".0%",
        xaxis_title="",
        yaxis_title="",
        yaxis=dict(categoryorder='total ascending'),
	margin=plot_margin
    )


    st.plotly_chart(fig, use_container_width=True)

