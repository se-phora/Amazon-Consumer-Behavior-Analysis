import pandas as pd

def get_age_group(age):
    if 18 <= age <= 24:
        return "18–24"
    elif 25 <= age <= 34:
        return "25–34"
    elif 35 <= age <= 44:
        return "35–44"
    elif 45 <= age <= 54:
        return "45–54"
    elif age >= 55:
        return "55+"

def clean_data():
    df = pd.read_csv("data/amazon_survey.csv")
    df["age_group"] = df["age"].apply(get_age_group)
    df_clean = df.drop("Timestamp", axis=1)  # pas de inplace ici
    return df_clean
