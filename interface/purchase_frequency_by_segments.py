import streamlit as st
import plotly.express as px
from interface.constants import amazon_color_palette

def display_purchase_frequency(df_clean):

    gender_options = df_clean["Gender"].unique().tolist()
    gender_options.insert(0, "All genders") 

    selected_gender = st.selectbox("Select Gender", options=gender_options)

    if selected_gender == "All genders":
        filtered_df = df_clean.copy()
    else:
        filtered_df = df_clean[df_clean["Gender"] == selected_gender]

    count_df = filtered_df.groupby(["age_group", "Purchase_Frequency"]).size().reset_index(name="Count")

    fig = px.bar(
        count_df,
        x="age_group",
        y="Count",
        color="Purchase_Frequency",
        color_discrete_sequence=amazon_color_palette,
        barmode="group",
        title=f"Buying Frequency Across Age Groups ({selected_gender})"
    )

    fig.update_layout(
        title_font_size=24,
	autosize=True,
        legend_title_text="",
    )

    st.plotly_chart(fig, use_container_width=True)