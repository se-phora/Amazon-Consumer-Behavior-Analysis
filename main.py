import streamlit as st
from interface.cart_abandonment_analysis import display_cart_abandonment
from interface.search_methods_analysis import display_search_methods
from interface.purchase_frequency_by_segments import display_purchase_frequency
from interface.gender_distribution import display_gender_distribution
from interface.age_group_distribution import display_age_group_distribution
from tools.data_processing import clean_data


def main():
    st.set_page_config(page_title="Amazon Consumer Behavior Analysis", layout="wide")

    st.sidebar.title("Amazon Consumer Behavior Analysis Dashboard")

    st.sidebar.markdown("""
    <hr style="margin-top: 30px; margin-bottom: 10px;">
    <p style='text-align: center; font-size: 14px;'>
        Created by 
        <a href="https://github.com/se-phora" target="_blank" style="text-decoration: none; color: #1f77b4;">
            <strong>Sephora M</strong> 
            <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg" 
                 alt="GitHub" width="16" style="vertical-align: middle; margin-left: 4px;">
        </a>
    </p>
    """, unsafe_allow_html=True)

    df_clean = clean_data()

    col1, col2 = st.columns(2)

    with col1:
        display_gender_distribution(df_clean)
        display_cart_abandonment(df_clean)

    with col2:
        display_age_group_distribution(df_clean)
        display_search_methods(df_clean)
        
    st.markdown("---")  
    display_purchase_frequency(df_clean)


if __name__ == "__main__":
    main()